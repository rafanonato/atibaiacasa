"""Gera um projeto HyperFrames por Reel a partir de pecas.py.

Cada projeto fica em producao/reels/<id>/ com index.html (1080x1920, 9:16),
hyperframes.json e os assets gerados por build_graficos.py.

Regras seguidas (skill /hyperframes):
- cada cena é um .clip com data-start e data-duration;
- animações são GSAP em timeline pausada, registrada em window.__timelines;
- sem Date.now, Math.random, rede ou timers; tudo depende do tempo da timeline;
- texto dentro da faixa 168 a 1330 px (safe zone do Reel);
- GSAP vem de producao/scripts/vendor e a fonte do sistema, sem CDN.

Uso: producao/.venv/bin/python producao/scripts/build_reels.py
Depois: cd producao/reels/<id> && npx hyperframes check && npx hyperframes render
"""

import html
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from pecas import PECAS  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PRODUCAO = os.path.join(RAIZ, "producao")
VENDOR = os.path.join(PRODUCAO, "scripts", "vendor")
# Arial não é redistribuída no repositório: a cópia vem do macOS.
FONTE_SISTEMA = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

MODELO_HYPERFRAMES = {
    "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
    "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry",
    "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"},
    "media": {"autoProxy": True},
    "authoringSkill": "hyperframes",
}


def gerar_cenas(cenas):
    """Monta as cenas em sequência, sem sobreposição, e devolve (html, duração total)."""
    blocos, inicio = [], 0.0
    for i, (foto, texto, dur) in enumerate(cenas, start=1):
        blocos.append(f"""
      <div id="cena-{i:02d}" class="clip cena" data-start="{inicio:.2f}" data-duration="{dur:.2f}" data-track-index="0">
        <img class="fundo" src="assets/{foto}-fundo.jpg" alt="" />
        <div class="quadro"><img class="frente" data-layout-allow-overflow src="assets/{foto}-frente.jpg" alt="" /></div>
        <p class="texto">{html.escape(texto)}</p>
      </div>""")
        inicio += dur
    return "".join(blocos), inicio


def gerar_animacao(cenas):
    """Ken Burns leve na foto e entrada suave do texto, em cada cena."""
    linhas, inicio = [], 0.0
    for i, (_, _, dur) in enumerate(cenas, start=1):
        cid = f"#cena-{i:02d}"
        linhas.append(f'tl.fromTo("{cid} .frente", {{ scale: 1.0 }}, {{ scale: 1.06, duration: {dur:.2f}, ease: "none" }}, {inicio:.2f});')
        linhas.append(f'tl.fromTo("{cid} .texto", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power2.out" }}, {inicio:.2f});')
        inicio += dur
    return "\n      ".join(linhas)


def html_reel(peca):
    cenas_html, duracao = gerar_cenas(peca["cenas"])
    animacao = gerar_animacao(peca["cenas"])
    return f"""<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>{html.escape(peca["titulo"])}</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{
        font-family: "ArialBold";
        src: url("assets/fonts/Arial-Bold.ttf") format("truetype");
        font-weight: 700;
      }}
      :root {{
        --ink: #ffffff;
        --ground: #000000;
        --font-display: "ArialBold", Arial, sans-serif;
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        background: var(--ground);
      }}
      #root {{
        position: relative;
        width: 1080px;
        height: 1920px;
        font-family: var(--font-display);
        color: var(--ink);
      }}
      .cena {{
        position: absolute;
        inset: 0;
        overflow: hidden;
      }}
      .fundo {{
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        object-fit: cover;
      }}
      .quadro {{
        position: absolute;
        left: 0;
        top: 440px;
        width: 1080px;
        height: 1040px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }}
      .frente {{
        width: 1080px;
        height: auto;
        max-height: 1040px;
        object-fit: contain;
        transform-origin: center center;
      }}
      .texto {{
        position: absolute;
        left: 80px;
        right: 80px;
        top: 230px;
        text-align: center;
        font-size: 84px;
        line-height: 1.15;
        font-weight: 700;
        text-shadow: 0 4px 18px rgba(0, 0, 0, 0.55);
      }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="{duracao:.2f}"
      data-width="1080"
      data-height="1920"
    >{cenas_html}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {animacao}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""


def montar(peca):
    pasta = os.path.join(PRODUCAO, "reels", peca["id"])
    os.makedirs(os.path.join(pasta, "assets", "fonts"), exist_ok=True)
    shutil.copy(os.path.join(VENDOR, "gsap.min.js"), os.path.join(pasta, "assets", "gsap.min.js"))
    shutil.copy(FONTE_SISTEMA, os.path.join(pasta, "assets", "fonts", "Arial-Bold.ttf"))
    with open(os.path.join(pasta, "hyperframes.json"), "w", encoding="utf-8") as f:
        json.dump(MODELO_HYPERFRAMES, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(pasta, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_reel(peca))
    _, duracao = gerar_cenas(peca["cenas"])
    print(f"{peca['id']}: {len(peca['cenas'])} cenas, {duracao:.1f} s")


def main():
    for peca in PECAS:
        if peca["tipo"] == "reel":
            montar(peca)


if __name__ == "__main__":
    main()
