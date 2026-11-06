"""Gera o calendário do primeiro trimestre de 2027 a partir de pecas.py.

Saídas:
- producao/calendario/calendario-2027-t1.csv   (para importar em planilha ou agenda)
- docs/calendario-2027-t1.md                  (para leitura e aprovação)

As semanas 1 a 4 têm as peças prontas. As semanas 5 a 13 aparecem só com o tema.
Horário é uma hipótese (19h) até haver dado de horário de pico do público.

Uso: producao/.venv/bin/python producao/scripts/gerar_calendario.py
"""

import csv
import glob
import os
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(__file__))
from pecas import PECAS, SEMANAS_FUTURAS  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PRODUCAO = os.path.join(RAIZ, "producao")
HORARIO_HIPOTESE = "19:00 (hipótese, validar com dados de pico)"
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def arquivo_principal(peca):
    if peca["tipo"] == "reel":
        videos = sorted(glob.glob(os.path.join(PRODUCAO, "reels", peca["id"], "renders", "*.mp4")))
        return os.path.relpath(videos[-1], RAIZ) if videos else "não renderizado"
    if peca["tipo"] == "carrossel":
        return os.path.relpath(os.path.join(PRODUCAO, "graficos", peca["id"]), RAIZ) + "/"
    return os.path.relpath(os.path.join(PRODUCAO, "graficos", peca["id"], "story.jpg"), RAIZ)


def status(peca):
    if peca.get("bloqueio"):
        return "BLOQUEADA: " + peca["bloqueio"]
    if peca["tipo"] == "story":
        return "pronta: adicionar adesivo de enquete no app"
    return "pronta para validação"


def linhas_primeiro_mes():
    linhas = []
    for p in PECAS:
        linhas.append({
            "data": p["data"],
            "dia": DIAS[date.fromisoformat(p["data"]).weekday()],
            "horario": HORARIO_HIPOTESE,
            "tipo": p["tipo"],
            "id": p["id"],
            "titulo": p["titulo"],
            "arquivo": arquivo_principal(p),
            "legenda": p.get("legenda", ""),
            "status": status(p),
        })
    return linhas


def linhas_semanas_futuras():
    linhas = []
    for semana, inicio, tema, pilar in SEMANAS_FUTURAS:
        data = date.fromisoformat(inicio)
        linhas.append({
            "data": f"{data.isoformat()} (semana {semana})",
            "dia": "",
            "horario": "",
            "tipo": "a definir",
            "id": f"semana-{semana:02d}",
            "titulo": tema,
            "arquivo": "",
            "legenda": "",
            "status": f"a produzir (pilar: {pilar})",
        })
    return linhas


def escrever_csv(linhas, caminho):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    campos = ["data", "dia", "horario", "tipo", "id", "titulo", "arquivo", "legenda", "status"]
    with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        escritor.writeheader()
        escritor.writerows(linhas)


def escrever_markdown(primeiras, futuras, caminho):
    linhas = [
        "# Calendário do primeiro trimestre de 2027",
        "",
        "Status: **pronto para validação**. Nada foi publicado.",
        "",
        "Gerado por `producao/scripts/gerar_calendario.py` a partir de `producao/scripts/pecas.py`. Não editar à mão: altere `pecas.py` e rode o script de novo.",
        "",
        "Horário: 19h é uma hipótese até haver dado de pico do público. A publicação via Windsor precisa de URL pública; até lá, a publicação é manual.",
        "",
        "## Semanas 1 a 4: peças prontas",
        "",
        "| Data | Dia | Tipo | Peça | Arquivo | Status |",
        "|---|---|---|---|---|---|",
    ]
    for l in primeiras:
        linhas.append(f"| {l['data']} | {l['dia']} | {l['tipo']} | {l['titulo']} (`{l['id']}`) | `{l['arquivo']}` | {l['status']} |")
    linhas += ["", "## Legendas aprovadas", ""]
    for l in primeiras:
        linhas += [f"### {l['data']} · {l['titulo']} ({l['tipo']})", "", f"> {l['legenda']}", ""]
    linhas += [
        "## Semanas 5 a 13: tema do trimestre",
        "",
        "| Semana | Início | Tema | Pilar | Status |",
        "|---|---|---|---|---|",
    ]
    for semana, inicio, tema, pilar in SEMANAS_FUTURAS:
        linhas.append(f"| {semana} | {inicio} | {tema} | {pilar} | a produzir |")
    linhas.append("")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))


def main():
    primeiras = linhas_primeiro_mes()
    futuras = linhas_semanas_futuras()
    escrever_csv(primeiras + futuras, os.path.join(PRODUCAO, "calendario", "calendario-2027-t1.csv"))
    escrever_markdown(primeiras, futuras, os.path.join(RAIZ, "docs", "calendario-2027-t1.md"))
    print(f"{len(primeiras)} peças do primeiro mês, {len(futuras)} semanas com tema")


if __name__ == "__main__":
    main()
