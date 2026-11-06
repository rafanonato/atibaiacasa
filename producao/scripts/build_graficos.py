"""Gera as imagens das peças a partir das fotos do anúncio.

Saídas:
- producao/graficos/<carrossel-id>/slide-NN.jpg   (1080x1350, feed 4:5)
- producao/graficos/<story-id>/story.jpg          (1080x1920)
- producao/reels/<reel-id>/assets/<foto>-fundo.jpg   (1080x1920, fundo desfocado)
- producao/reels/<reel-id>/assets/<foto>-frente.jpg  (foto inteira, sem corte)

Método: a foto inteira fica centralizada sobre uma cópia desfocada dela mesma.
Assim a resolução de 1200 px não é esticada para 9:16 nem cortada.

Uso: producao/.venv/bin/python producao/scripts/build_graficos.py
"""

import os
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from pecas import ARQUIVO_FOTOS, HANDLE, PECAS  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FOTOS = os.path.join(RAIZ, ARQUIVO_FOTOS)
PRODUCAO = os.path.join(RAIZ, "producao")

FONTE_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONTE_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

BRANCO = (255, 255, 255)
SOMBRA = (0, 0, 0, 170)


def abrir_foto(nome):
    return Image.open(os.path.join(FOTOS, f"{nome}.jpeg")).convert("RGB")


def fundo_desfocado(img, largura, altura):
    """Preenche o quadro com a foto esticada para cobrir, desfocada e escurecida."""
    escala = max(largura / img.width, altura / img.height)
    cobre = img.resize((round(img.width * escala), round(img.height * escala)), Image.LANCZOS)
    x = (cobre.width - largura) // 2
    y = (cobre.height - altura) // 2
    cobre = cobre.crop((x, y, x + largura, y + altura))
    cobre = cobre.filter(ImageFilter.GaussianBlur(45))
    return ImageEnhance.Brightness(cobre).enhance(0.5)


def frente(img, caixa_w, caixa_h):
    """Foto inteira, reduzida para caber na caixa, sem corte."""
    escala = min(caixa_w / img.width, caixa_h / img.height)
    return img.resize((round(img.width * escala), round(img.height * escala)), Image.LANCZOS)


def quebrar_linhas(draw, texto, fonte, largura_max):
    palavras = texto.split()
    linhas, atual = [], ""
    for p in palavras:
        teste = f"{atual} {p}".strip()
        if draw.textlength(teste, font=fonte) <= largura_max:
            atual = teste
        else:
            linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def escrever_centro(img, texto, y_topo, tamanho, largura_max, fonte_path=FONTE_BOLD):
    draw = ImageDraw.Draw(img, "RGBA")
    fonte = ImageFont.truetype(fonte_path, tamanho)
    linhas = quebrar_linhas(draw, texto, fonte, largura_max)
    passo = int(tamanho * 1.15)
    y = y_topo
    for linha in linhas:
        w = draw.textlength(linha, font=fonte)
        x = (img.width - w) / 2
        draw.text((x + 3, y + 4), linha, font=fonte, fill=SOMBRA)
        draw.text((x, y), linha, font=fonte, fill=BRANCO)
        y += passo
    return y


def slide_carrossel(foto_nome, texto, indice, total, capa=False):
    W, H = 1080, 1350
    base = fundo_desfocado(abrir_foto(foto_nome), W, H)
    img = base.convert("RGBA")
    foto = frente(abrir_foto(foto_nome), 1000, 680).convert("RGBA")
    img.paste(foto, ((W - foto.width) // 2, 520), foto)
    escrever_centro(img, texto, 150, 96 if capa else 72, 900)
    draw = ImageDraw.Draw(img, "RGBA")
    fonte = ImageFont.truetype(FONTE_REG, 38)
    rodape = f"{HANDLE}   {indice}/{total}"
    w = draw.textlength(rodape, font=fonte)
    draw.text(((W - w) / 2, 1230), rodape, font=fonte, fill=BRANCO)
    return img.convert("RGB")


def story_pergunta(foto_nome, texto):
    W, H = 1080, 1920
    img = fundo_desfocado(abrir_foto(foto_nome), W, H).convert("RGBA")
    escrever_centro(img, texto, 760, 112, 900)
    draw = ImageDraw.Draw(img, "RGBA")
    fonte = ImageFont.truetype(FONTE_REG, 42)
    w = draw.textlength(HANDLE, font=fonte)
    draw.text(((W - w) / 2, 1560), HANDLE, font=fonte, fill=BRANCO)
    return img.convert("RGB")


def reel_assets(reel):
    destino = os.path.join(PRODUCAO, "reels", reel["id"], "assets")
    os.makedirs(destino, exist_ok=True)
    fotos = sorted({cena[0] for cena in reel["cenas"]})
    for nome in fotos:
        img = abrir_foto(nome)
        fundo_desfocado(img, 1080, 1920).save(os.path.join(destino, f"{nome}-fundo.jpg"), quality=92)
        frente(img, 1080, 1040).save(os.path.join(destino, f"{nome}-frente.jpg"), quality=92)
    return fotos


def main():
    for peca in PECAS:
        if peca["tipo"] == "carrossel":
            pasta = os.path.join(PRODUCAO, "graficos", peca["id"])
            os.makedirs(pasta, exist_ok=True)
            total = len(peca["slides"])
            for i, (foto, texto) in enumerate(peca["slides"], start=1):
                slide_carrossel(foto, texto, i, total, capa=(i == 1)).save(
                    os.path.join(pasta, f"slide-{i:02d}.jpg"), quality=92
                )
            print(f"{peca['id']}: {total} slides")
        elif peca["tipo"] == "story":
            pasta = os.path.join(PRODUCAO, "graficos", peca["id"])
            os.makedirs(pasta, exist_ok=True)
            story_pergunta(peca["foto"], peca["texto"]).save(os.path.join(pasta, "story.jpg"), quality=92)
            print(f"{peca['id']}: story")
        elif peca["tipo"] == "reel":
            fotos = reel_assets(peca)
            print(f"{peca['id']}: assets de {len(fotos)} fotos")


if __name__ == "__main__":
    main()
