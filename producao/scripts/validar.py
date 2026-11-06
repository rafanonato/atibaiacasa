"""Valida as peças antes da publicação: arquivos, dimensões, duração e legendas.

Checagens de legenda seguem a lista do ig-humanizer (modo audit) e as regras do
planejamento: sem travessão em excesso, sem vocabulário de IA, gancho nos primeiros
125 caracteres, até 2.200 caracteres, 0 a 3 emojis e chamada para ação.

Saída: tabela em stdout. Sai com código 1 se houver erro bloqueante.

Uso: producao/.venv/bin/python producao/scripts/validar.py
"""

import glob
import json
import os
import re
import subprocess
import sys
from datetime import date

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from pecas import PECAS  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PRODUCAO = os.path.join(RAIZ, "producao")

# Vocabulário que costuma marcar texto escrito por IA em português (lista de trabalho).
VOCAB_IA = [
    "alavancar", "significativo", "elevar", "mergulhar", "potencializar", "robusto",
    "crucial", "vibrante", "transformador", "jornada", "revolucionar", "essencial",
    "destacar-se", "navegar", "ecossistema", "sinergia",
]
CTA = re.compile(r"(reserv|datas|veja|confira|escolha|salve|quer ver|chegou)", re.IGNORECASE)
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")


def dias_semana(iso):
    nomes = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    return nomes[date.fromisoformat(iso).weekday()]


def checar_legenda(texto):
    erros, avisos = [], []
    if texto is None:
        return ["sem legenda"], []
    tamanho = len(texto)
    if tamanho > 2200:
        erros.append(f"legenda com {tamanho} caracteres (limite 2.200)")
    primeiros = texto[:125]
    if not CTA.search(texto):
        avisos.append("sem chamada para ação reconhecível")
    travessoes = texto.count("—")
    if travessoes > 1:
        avisos.append(f"{travessoes} travessões")
    emojis = len(EMOJI.findall(texto))
    if emojis > 3:
        avisos.append(f"{emojis} emojis (recomendado 0 a 3)")
    achados = [p for p in VOCAB_IA if re.search(rf"\b{p}\b", texto, re.IGNORECASE)]
    if achados:
        avisos.append("vocabulário de IA: " + ", ".join(achados))
    hashtags = len(re.findall(r"#\w+", texto))
    if hashtags == 0:
        avisos.append("sem hashtags (sugerido 3 a 5, a definir com ig-hashtag-strategist)")
    elif hashtags > 5:
        avisos.append(f"{hashtags} hashtags (recomendado 3 a 5)")
    return erros, avisos, tamanho, primeiros


def dimensao(caminho):
    with Image.open(caminho) as im:
        return im.size


def tem_audio(caminho):
    saida = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=codec_name",
         "-of", "csv=p=0", caminho],
        capture_output=True, text=True, check=True,
    )
    return bool(saida.stdout.strip())


def video_info(caminho):
    saida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "stream=width,height,r_frame_rate",
         "-show_entries", "format=duration", "-of", "json", caminho],
        capture_output=True, text=True, check=True,
    )
    dados = json.loads(saida.stdout)
    video = next(s for s in dados["streams"] if "width" in s)
    return int(video["width"]), int(video["height"]), float(dados["format"]["duration"])


def ultimo_render(peca_id):
    arquivos = sorted(glob.glob(os.path.join(PRODUCAO, "reels", peca_id, "renders", "*.mp4")))
    return arquivos[-1] if arquivos else None


def verificar_peca(peca):
    erros, avisos = [], []
    legenda = peca.get("legenda")
    if peca["tipo"] == "carrossel":
        pasta = os.path.join(PRODUCAO, "graficos", peca["id"])
        slides = sorted(glob.glob(os.path.join(pasta, "slide-*.jpg")))
        if len(slides) != len(peca["slides"]):
            erros.append(f"{len(slides)} slides gerados de {len(peca['slides'])}")
        for s in slides:
            if dimensao(s) != (1080, 1350):
                erros.append(f"{os.path.basename(s)} fora de 1080x1350")
        arquivo = os.path.relpath(pasta, RAIZ)
        detalhe = f"{len(slides)} slides 4:5"
    elif peca["tipo"] == "story":
        caminho = os.path.join(PRODUCAO, "graficos", peca["id"], "story.jpg")
        if not os.path.exists(caminho) or dimensao(caminho) != (1080, 1920):
            erros.append("story ausente ou fora de 1080x1920")
        arquivo = os.path.relpath(caminho, RAIZ)
        detalhe = "1080x1920"
        legenda = None
    else:
        video = ultimo_render(peca["id"])
        if not video:
            erros.append("sem MP4 renderizado")
            arquivo, detalhe = "-", "-"
        else:
            largura, altura, duracao = video_info(video)
            if (largura, altura) != (1080, 1920):
                erros.append(f"vídeo {largura}x{altura}, esperado 1080x1920")
            esperado = sum(c[2] for c in peca["cenas"])
            if abs(duracao - esperado) > 0.3:
                erros.append(f"duração {duracao:.1f}s, esperado {esperado:.1f}s")
            arquivo = os.path.relpath(video, RAIZ)
            if tem_audio(video):
                detalhe = f"1080x1920, {duracao:.1f} s, com trilha"
            else:
                detalhe = f"1080x1920, {duracao:.1f} s, sem som"
                avisos.append("sem trilha sonora")
    resultado = {"id": peca["id"], "data": peca["data"], "dia": dias_semana(peca["data"]),
                 "tipo": peca["tipo"], "arquivo": arquivo, "detalhe": detalhe,
                 "erros": erros, "avisos": avisos}
    if legenda is not None:
        ret = checar_legenda(legenda)
        if isinstance(ret, tuple) and len(ret) == 4:
            e, a, tamanho, gancho = ret
            resultado["erros"] += e
            resultado["avisos"] += a
            resultado["legenda_caracteres"] = tamanho
            resultado["gancho"] = gancho
    if peca.get("bloqueio"):
        resultado["avisos"].append("BLOQUEADA: " + peca["bloqueio"])
    return resultado


def main():
    resultados = [verificar_peca(p) for p in PECAS]
    bloqueantes = 0
    print("| Data | Dia | Peça | Arquivo | Erros | Avisos |")
    print("|---|---|---|---|---|---|")
    for r in resultados:
        bloqueantes += len(r["erros"])
        print(f"| {r['data']} | {r['dia']} | {r['id']} | {r['arquivo']} | "
              f"{'; '.join(r['erros']) or 'nenhum'} | {'; '.join(r['avisos']) or 'nenhum'} |")
    print()
    print("Gancho (primeiros 125 caracteres) e tamanho das legendas:")
    for r in resultados:
        if "gancho" in r:
            print(f"- {r['id']} ({r['legenda_caracteres']} caracteres): {r['gancho']}")
    return 1 if bloqueantes else 0


if __name__ == "__main__":
    sys.exit(main())
