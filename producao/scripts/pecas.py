"""Fonte única das peças de engajamento e alcance (novembro e dezembro de 2026).

Objetivo: aumentar alcance e engajamento agora, para levar hóspedes para as datas
livres de janeiro a março de 2027. Carnaval e o fim de semana da virada já estão
reservados, então não são promovidos. A reserva de 8 a 10/1 aparece na planilha
e precisa de confirmação.

Usada por build_graficos.py, build_reels.py, gerar_calendario.py e validar.py.
Fotos: IDs de `docs/Fotos do anúncio Airbnb/foto-NN.jpeg`.
"""

ARQUIVO_FOTOS = "docs/Fotos do anúncio Airbnb"

HANDLE = "@atibaiacasa"

# Hashtags aprovadas em 06/11/2026 para Reels e carrosséis (sem story).
HASHTAGS = "#atibaia #viagememfamilia #lazeremfamilia"

# Trilhas em docs/sons/ (fornecidas pelo dono). Cada Reel recebe um trecho com
# fade de saída. Os nomes indicam a fonte Pixabay; confirmar a licença antes de publicar.
_GRAND = "grand_project-toward-the-dream-uplifting-orchestral-adventure-full-2m52s-628698.mp3"
_BROTHER = "brotheration_records-everyday-is-a-holiday-queens-of-ocean-11-brotheration-records-325618.mp3"
TRILHAS = {
    "reel-01-piscina": (_GRAND, 0),
    "reel-02-avaliacoes": (_BROTHER, 0),
    "reel-03-terca-quinta": (_BROTHER, 15),
    "reel-04-chegando": (_GRAND, 20),
    "reel-06-escolha-fim-de-semana": (_GRAND, 40),
    "reel-05-cozinha": (_BROTHER, 30),
    "reel-07-marque-quem": (_BROTHER, 50),
}

PECAS = [
    {
        "id": "reel-01-piscina",
        "data": "2026-11-07",
        "tipo": "reel",
        "titulo": "Piscina com vista",
        "cenas": [
            ("foto-03", "Piscina aquecida em Atibaia?", 3),
            ("foto-03", "Aquecimento sob solicitação, sem custo", 3),
            ("foto-56", "Piscina de 70 cm a 1,5 m", 3),
            ("foto-46", "Vista de cima", 3),
            ("foto-55", "Fogueira no fim de semana", 3),
            ("foto-12", "Veja as datas no Airbnb", 3),
        ],
        "legenda": (
            "Piscina aquecida em Atibaia, sem pagar a mais pelo aquecimento. Fica ligada quando "
            "você pedir. A casa tem área de lazer, com campo e espaço para toda a família. "
            "Qual fim de semana você escolhe? Comente abaixo. " + HANDLE
        ),
    },
    {
        "id": "story-09-11-enquete",
        "data": "2026-11-09",
        "tipo": "story",
        "titulo": "Janeiro ou fevereiro?",
        "foto": "foto-03",
        "texto": "Janeiro ou fevereiro?",
        "observacao": "Adicionar o adesivo de enquete no app, com as opções Janeiro e Fevereiro.",
    },
    {
        "id": "carrossel-01-o-que-tem",
        "data": "2026-11-11",
        "tipo": "carrossel",
        "titulo": "O que tem na casa",
        "slides": [
            ("foto-01", "O que tem na Casa Atibaia"),
            ("foto-03", "Piscina aquecida, sob solicitação, sem custo"),
            ("foto-12", "Mesa grande para jantar em família"),
            ("foto-23", "Área gourmet com churrasqueira e forno"),
            ("foto-29", "Sala com vista para o jardim"),
            ("foto-14", "Cozinha completa com bancada de mármore"),
            ("foto-07", "Quartos em suíte"),
            ("foto-61", "Veja as datas no Airbnb"),
        ],
        "legenda": (
            "Piscina, campo, área gourmet, sala com vista para o jardim e cozinha completa. "
            "Salve para o seu próximo fim de semana em família. Qual desses espaços você mais "
            "quer ver? Comente. " + HANDLE
        ),
    },
    {
        "id": "reel-02-avaliacoes",
        "data": "2026-11-13",
        "tipo": "reel",
        "titulo": "40 avaliações",
        "cenas": [
            ("foto-29", "Nota 4,75", 3.75),
            ("foto-27", "40 avaliações de hóspedes", 3.75),
            ("foto-14", "Hospitalidade, espaço e família são o que mais aparece", 3.75),
            ("foto-44", "Veja as datas disponíveis", 3.75),
        ],
        "legenda": (
            "A casa tem nota 4,75 com 40 avaliações no Airbnb. Quem já ficou aqui fala de "
            "hospitalidade e de espaço. Quer saber o que mais pesa na escolha? Pergunte aqui "
            "que a gente responde. " + HANDLE
        ),
    },
    {
        "id": "reel-03-terca-quinta",
        "data": "2026-11-16",
        "tipo": "reel",
        "titulo": "Terça a quinta",
        "cenas": [
            ("foto-44", "Entrada e saída mais flexíveis", 3),
            ("foto-61", "Terça a quinta, com mínimo de 2 noites", 3),
            ("foto-05", "Sexta a domingo, mínimo de 2 noites", 3),
            ("foto-31", "Veja as datas no Airbnb", 3),
        ],
        "legenda": (
            "Terça, quarta ou quinta? Aqui a entrada e a saída são flexíveis, com mínimo de duas "
            "noites. Qual dia da semana funciona para a sua família? Comente. " + HANDLE
        ),
    },
    {
        "id": "carrossel-04-perguntas-frequentes",
        "data": "2026-11-18",
        "tipo": "carrossel",
        "titulo": "Perguntas frequentes",
        "slides": [
            ("foto-01", "Perguntas frequentes antes de reservar"),
            ("foto-27", "Check-in a partir das 12h. Check-out até as 18h."),
            ("foto-07", "Roupa de cama e banho não estão inclusas"),
            ("foto-58", "1 pet de cortesia. A partir do 2º pet, consulte a taxa."),
            ("foto-11", "Festas e eventos: combinamos antes, com taxa extra"),
            ("foto-56", "Piscina com aquecimento sob solicitação, sem custo"),
            ("foto-61", "Ainda com dúvida? Pergunte aqui ou no Airbnb"),
        ],
        "legenda": (
            "Dúvidas antes de reservar? Aqui vão as mais comuns. Salve este post e marque quem "
            "está planejando uma viagem. " + HANDLE
        ),
    },
    {
        "id": "reel-04-chegando",
        "data": "2026-11-20",
        "tipo": "reel",
        "titulo": "Chegando em Atibaia",
        "cenas": [
            ("foto-02", "Fachada e entrada", 3),
            ("foto-54", "Casa com jardim e palmeira", 3),
            ("foto-53", "Gramado amplo", 3),
            ("foto-20", "Estacionamento para 7 carros", 3),
            ("foto-01", "Chegou? Veja as datas no Airbnb", 3),
        ],
        "legenda": (
            "Chegou em Atibaia? A casa tem entrada pela frente, jardim e estacionamento para 7 "
            "carros. Confira as datas no Airbnb. Qual foi a sua primeira impressão? " + HANDLE
        ),
    },
    {
        "id": "reel-06-escolha-fim-de-semana",
        "data": "2026-11-23",
        "tipo": "reel",
        "titulo": "Escolha seu fim de semana",
        "cenas": [
            ("foto-29", "Confira as datas livres de janeiro", 3),
            ("foto-44", "Terça a quinta, entrada flexível", 3),
            ("foto-31", "Março tem emenda da Páscoa", 3),
            ("foto-61", "Veja as datas no Airbnb", 3),
        ],
        "legenda": (
            "Janeiro, fevereiro ou março? Confira as datas livres no Airbnb e escolha o seu fim "
            "de semana. Comente qual mês você escolhe. " + HANDLE
        ),
    },
    {
        "id": "carrossel-05-precos-2027",
        "data": "2026-11-25",
        "tipo": "carrossel",
        "titulo": "Quanto custa em 2027",
        "slides": [
            ("foto-01", "Diárias de 2027 por noite"),
            ("foto-29", "Janeiro a junho: terça a quinta, R$ 1.100"),
            ("foto-61", "Janeiro a junho: sexta e sábado, R$ 1.250"),
            ("foto-03", "Julho: R$ 1.150 de terça a quinta e R$ 1.350 na sexta e no sábado"),
            ("foto-44", "Emendas de feriado: R$ 1.400, com mínimo de 3 noites"),
            ("foto-31", "Valores antes das taxas. Confira o total no Airbnb."),
        ],
        "legenda": (
            "Quanto custa curtir a casa em 2027? Os valores por noite estão nos slides. Salve para "
            "planejar a viagem e comente qual fim de semana você escolheria. " + HANDLE
        ),
    },
    {
        "id": "reel-05-cozinha",
        "data": "2026-11-27",
        "tipo": "reel",
        "titulo": "Cozinha completa",
        "cenas": [
            ("foto-13", "Cozinha completa", 3),
            ("foto-14", "Bancada de mármore", 3),
            ("foto-36", "Pronta para cozinhar em família", 3),
            ("foto-39", "Fogão e geladeira", 3),
            ("foto-40", "Veja as datas no Airbnb", 3),
        ],
        "legenda": (
            "Cozinha completa com bancada de mármore. Quem gosta de cozinhar em família vai sentir "
            "a diferença. Quem cozinha por aí? Conte nos comentários. " + HANDLE
        ),
    },
    {
        "id": "reel-07-marque-quem",
        "data": "2026-11-30",
        "tipo": "reel",
        "titulo": "Marque quem",
        "cenas": [
            ("foto-03", "Marque quem merece um fim de semana assim", 3),
            ("foto-12", "Mesa grande para a turma", 3),
            ("foto-55", "Fogueira para a noite", 3),
            ("foto-46", "Comente qual é o seu plano", 3),
        ],
        "legenda": (
            "Marque quem você levaria para cá. Piscina, mesa grande e fogueira para a noite. Qual "
            "é o seu plano ideal? " + HANDLE
        ),
    },
    {
        "id": "carrossel-02-churrasco",
        "data": "2026-12-02",
        "tipo": "carrossel",
        "titulo": "Churrasco de domingo",
        "slides": [
            ("foto-23", "Churrasco de domingo"),
            ("foto-24", "Área gourmet com mesa de madeira para o almoço"),
            ("foto-25", "Área coberta com cozinha de apoio"),
            ("foto-57", "Coberta, com vista para o jardim"),
            ("foto-26", "Pia e bancada para o preparo"),
            ("foto-50", "Espaço coberto com vista para o verde"),
        ],
        "legenda": (
            "Área gourmet com churrasqueira e forno, mesa de madeira e vista para o verde. O "
            "domingo começa cedo por aqui. Quem assume o churrasco na sua família? " + HANDLE
        ),
    },
    {
        "id": "story-04-12-enquete",
        "data": "2026-12-04",
        "tipo": "story",
        "titulo": "Qual mês você quer vir?",
        "foto": "foto-29",
        "texto": "Qual mês você quer vir?",
        "observacao": "Adicionar o adesivo de enquete no app, com as opções Janeiro, Fevereiro e Março.",
    },
]

# Semanas de dezembro a março: tema e pilar. Foco em datas livres de janeiro a março.
# Carnaval e a virada já reservados: não são promovidos.
SEMANAS_FUTURAS = [
    (5, "2026-12-07", "Férias de verão em família: por que janeiro em Atibaia", "Família e amigos"),
    (6, "2026-12-14", "Dúvidas frequentes em vídeo", "Prova social"),
    (7, "2026-12-21", "Avaliação de hóspede (com autorização)", "Prova social"),
    (8, "2026-12-28", "Retrospectiva com as fotos da casa", "Engajamento"),
    (9, "2027-01-04", "Janeiro: fins de semana e terça a quinta com datas livres", "Datas"),
    (10, "2027-01-11", "Fevereiro: fins de semana livres, sem Carnaval", "Datas"),
    (11, "2027-01-18", "Março: emenda da Páscoa com preço de emenda", "Datas"),
    (12, "2027-01-25", "Ranking de memórias de férias (enquete)", "Engajamento"),
    (13, "2027-02-01", "Piscina e churrasco de fim de semana", "Experiência"),
]


# Hashtags entram no fim das legendas de Reels e carrosséis.
for _peca in PECAS:
    if "legenda" in _peca:
        _peca["legenda"] = f"{_peca['legenda']}\n\n{HASHTAGS}"
