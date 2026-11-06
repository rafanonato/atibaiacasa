"""Fonte única das peças do primeiro mês (semanas 1 a 4 de 2027).

Usada por build_graficos.py, build_reels.py e gerar_calendario.py.
Alterar um texto aqui e rodar os scripts de novo atualiza imagens, vídeos e calendário.

Fotos: IDs de `docs/Fotos do anúncio Airbnb/foto-NN.jpeg`.
Legendas: as aprovadas em docs/planejamento-primeiros-posts-e-reels.md.
Textos na tela de Reels: sem "link na bio" enquanto a bio aponta para a Keepo.
"""

ARQUIVO_FOTOS = "docs/Fotos do anúncio Airbnb"

HANDLE = "@atibaiacasa"

# Cada peça: data, tipo, fotos, texto de cada cena/slide, legenda.
# Para reels, "cenas" = lista de (foto, texto_na_tela, segundos).
# Para carrosséis, "slides" = lista de (foto, título). O primeiro slide é a capa.
PECAS = [
    {
        "id": "reel-01-piscina",
        "data": "2027-01-04",
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
            "Piscina aquecida em Atibaia, sem pagar a mais pelo aquecimento. "
            "Fica ligada quando você pedir. Casa na área de lazer, com campo e espaço "
            "para toda a família. Qual fim de semana você escolhe? " + HANDLE
        ),
    },
    {
        "id": "carrossel-01-o-que-tem",
        "data": "2027-01-06",
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
            "Salve para o seu próximo fim de semana em família. " + HANDLE
        ),
    },
    {
        "id": "reel-02-avaliacoes",
        "data": "2027-01-08",
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
            "hospitalidade e de espaço. Quer ver as datas? " + HANDLE
        ),
    },
    {
        "id": "reel-03-terca-quinta",
        "data": "2027-01-11",
        "tipo": "reel",
        "titulo": "Terça a quinta",
        "cenas": [
            ("foto-44", "Entrada e saída mais flexíveis", 3),
            ("foto-61", "Terça a quinta, com mínimo de 2 noites", 3),
            ("foto-05", "Sexta a domingo, mínimo de 2 noites", 3),
            ("foto-31", "Veja as datas no Airbnb", 3),
        ],
        "legenda": (
            "Terça, quarta ou quinta? Aqui a entrada e a saída são flexíveis, com mínimo de "
            "duas noites. Escolha o melhor dia para a sua família. " + HANDLE
        ),
    },
    {
        "id": "story-13-01-enquete",
        "data": "2027-01-13",
        "tipo": "story",
        "titulo": "Janeiro ou fevereiro?",
        "foto": "foto-03",
        "texto": "Janeiro ou fevereiro?",
        "observacao": "Adesivo de enquete é adicionado manualmente no app do Instagram.",
    },
    {
        "id": "carrossel-02-churrasco",
        "data": "2027-01-20",
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
            "Área gourmet com churrasqueira e forno, mesa de madeira e vista para o verde. "
            "O domingo começa cedo por aqui. " + HANDLE
        ),
    },
    {
        "id": "reel-04-chegando",
        "data": "2027-01-22",
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
            "Chegou em Atibaia? A casa tem entrada pela frente, jardim e estacionamento "
            "para 7 carros. Confira as datas no Airbnb. " + HANDLE
        ),
    },
    {
        "id": "reel-05-cozinha",
        "data": "2027-01-25",
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
            "Cozinha completa com bancada de mármore. Quem gosta de cozinhar em família "
            "vai sentir a diferença. " + HANDLE
        ),
    },
    {
        "id": "carrossel-03-carnaval",
        "data": "2027-01-27",
        "tipo": "carrossel",
        "titulo": "Carnaval em casa",
        "bloqueio": "Reserva existente de 5 a 9/2. Só publicar após confirmar disponibilidade no Airbnb.",
        "slides": [
            ("foto-03", "Carnaval em casa com a turma"),
            ("foto-46", "Piscina vista de cima"),
            ("foto-11", "Sala com vista para a piscina"),
            ("foto-12", "Mesa comprida para a turma"),
            ("foto-29", "Sala ampla para a noite"),
            ("foto-61", "Reserve de 5 a 9 de fevereiro"),
        ],
        "legenda": (
            "Carnaval em Atibaia com a turma. Reserve de 5 a 9 de fevereiro. "
            "Vagas por ordem de reserva. " + HANDLE
        ),
    },
]

# Semanas 5 a 13: só tema, a produzir depois do primeiro mês.
# (semana, início, tema, pilar)
SEMANAS_FUTURAS = [
    (5, "2027-02-01", "Carnaval: chamada para 5 a 9/2", "Datas e emendas"),
    (6, "2027-02-08", "Carnaval: bastidor e pós-Carnaval", "Família e amigos"),
    (7, "2027-02-15", "Avaliação de hóspede (com autorização)", "Prova social"),
    (8, "2027-02-22", "Fim de férias e volta às aulas", "Família e amigos"),
    (9, "2027-03-01", "Chamada para a emenda de Sexta-feira Santa", "Datas e emendas"),
    (10, "2027-03-08", "Escapada entre amigas (Dia das Mulheres)", "Datas e emendas"),
    (11, "2027-03-15", "Sexta-feira Santa e Páscoa: carrossel da emenda", "Datas e emendas"),
    (12, "2027-03-22", "Páscoa: chamada para 25 a 28/3", "Datas e emendas"),
    (13, "2027-03-29", "Fechamento do trimestre e prévia do segundo", "Atibaia"),
]
