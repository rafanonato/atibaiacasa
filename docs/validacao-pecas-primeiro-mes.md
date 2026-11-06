# Validação das peças do primeiro mês (semanas 1 a 4 de 2027)

Status: **pronto para validação**. Nada foi publicado. Data: 2026-11-06.

## O que foi produzido

| Tipo | Quantidade | Onde fica |
|---|---|---|
| Reels (MP4, 1080×1920, 30 fps, sem som) | 5 | `producao/reels/<id>/renders/` |
| Carrosséis (JPEG, 1080×1350) | 3 (20 slides) | `producao/graficos/<id>/` |
| Story (JPEG, 1080×1920) | 1 | `producao/graficos/story-13-01-enquete/story.jpg` |
| Calendário | 13 semanas | `docs/calendario-2027-t1.md` e `producao/calendario/calendario-2027-t1.csv` |

Projetos HyperFrames dos Reels (com o código da cena): `producao/reels/<id>/`.

## Como foi feito

- **Fonte única:** `producao/scripts/pecas.py`. Textos, legendas, fotos e datas estão só aí. Os outros scripts leem dali.
- **Imagens:** `build_graficos.py`. Usa Pillow. A foto inteira fica centralizada sobre uma cópia desfocada dela mesma, para não perder resolução.
- **Reels:** `build_reels.py` gera um projeto HyperFrames por Reel. Usa a skill `/hyperframes` como base. GSAP e a fonte Arial Bold ficam dentro do projeto, sem CDN, para o render funcionar offline.
- **Calendário:** `gerar_calendario.py`.
- **Validação:** `validar.py`. Confere arquivos, dimensões, duração e legendas.

Para refazer tudo depois de mudar um texto:

```bash
producao/.venv/bin/python producao/scripts/build_graficos.py
producao/.venv/bin/python producao/scripts/build_reels.py
producao/.venv/bin/python producao/scripts/gerar_calendario.py
producao/.venv/bin/python producao/scripts/validar.py
```

Depois, para cada Reel: `cd producao/reels/<id> && npx hyperframes@0.9.19 render`.

## Resultado da validação automática

Rodada de `validar.py`:

- **Erros bloqueantes:** nenhum.
- **Dimensões e duração:** todos os Reels em 1080×1920 e com a duração prevista. Todos os slides em 1080×1350. Story em 1080×1920.
- **Bloqueio:** carrossel do Carnaval (27/1). Existe reserva de 5 a 9/2. Só publicar depois de confirmar a disponibilidade no Airbnb.
- **Avisos (não bloqueiam):**
  - Sem trilha sonora nos Reels (ver pendências).
  - Sem hashtags nas legendas (ver pendências).
  - Algumas legendas sem chamada para ação reconhecível pelo script. Conferido à mão: a chamada existe em quase todas, e o script pode não reconhecer a forma escrita.

Checagem do HyperFrames: `check` sem erros em todos os Reels. Os avisos são de estrutura (o lint sugere separar cada cena em sub-composição) e de som. Não impedem o render.

## Checagem das legendas (lista do ig-humanizer)

| Item | Resultado |
|---|---|
| Travessões | nenhum |
| Vocabulário de IA | nenhum dos termos da lista |
| Gancho nos primeiros 125 caracteres | todos têm o gancho dentro do limite |
| Tamanho | todas abaixo de 2.200 caracteres (a maior tem 203) |
| Emojis | nenhum (dentro do recomendado de 0 a 3) |
| Chamada para ação | presente na maioria |
| Hashtags | nenhuma (ver pendências) |

## Ajustes feitos durante a validação

1. **Carrossel do Carnaval:** a foto 56 repetia a 03, então o slide 2 passou a usar a 46 (vista de cima da piscina).
2. **Capa dos carrosséis:** o título encostava na foto. Subi a foto e fixei o título no topo.
3. **Reel 1:** "1,5 m" quebrava a linha antes do "m". Agora usa espaço inseparável.
4. **Reel 1:** o slide "Vista de cima" usava a foto 56. Passou a usar a 46, que é a vista aérea.
5. **Reel 5:** "Fogão, forno e geladeira" virou "Fogão e geladeira", porque não consegui confirmar o forno na foto 39.
6. **CTA "Reserve pelo link na bio":** trocado por "Veja as datas no Airbnb", porque a bio ainda aponta para a Keepo. Aprovado.
7. **Legenda do Reel 1:** "A casa tem área de lazer, com campo e espaço para toda a família." Aprovado.
8. **Trilha e hashtags** aplicadas nos Reels e legendas. Validação atualizada: todos os Reels com áudio.

## Pontos a confirmar com você

- **Campo de futebol:** não consegui identificar a foto do campo com segurança. O Reel 4 usa "Gramado amplo" no lugar. Pendente.
- **Estacionamento para 7 carros:** o Reel 4 usa a foto 20 (entrada com pavimento). Não tenho certeza de que mostra as vagas.
- **Pessoas nas fotos:** Rafael confirmou que não há pessoas nas fotos.
- **Quartos em suíte:** o slide 7 do primeiro carrossel usa a foto 07 (quarto). A palavra "suíte" vem da listagem, não da foto.


## Pendências antes de publicar

1. **Trilha sonora.** Aplicada: as 3 faixas de `docs/sons/` foram cortadas e colocadas nos Reels. Confirmar a licença (os nomes indicam Pixabay).
2. **Hashtags.** Aprovadas e incluídas: #atibaia #viagememfamilia #lazeremfamilia. Não foi possível dimensionar o volume de cada uma (sem Apify).
3. **Método de publicação.** Opções:
   - **Manual** pelo app, com os arquivos prontos. É o caminho mais simples para começar.
   - **Via Windsor.** Exige URL pública para cada imagem ou vídeo (carrossel: de 2 a 10 imagens; Reel: MP4; story: imagem). O repositório é privado, então não serve para hospedar. Precisa de um repositório público separado só com as peças prontas, ou de outro serviço de hospedagem.
4. **Adesivo de enquete no story de 13/1.** Não será adicionado (aprovado sem adesivo).
5. **Horário.** 19h é hipótese. Sem dado de pico, o horário pode ficar fora do momento em que o público está ativo.
6. **Bio do Instagram** apontando para o Airbnb. Sem isso, o CTA "link na bio" não existe, e os textos já estão adaptados para não depender dele.
7. **Confirmar disponibilidade do Carnaval** no Airbnb antes do carrossel de 27/1.

## Publicação: pedido de começar em 07/11/2026

Pedido: executar o planejamento no Windsor a partir de amanhã. Não foi executado ainda, por três motivos (ver `docs/decisoes.md`): o Windsor publica na hora e não agenda; as mídias precisariam de URL pública; e o calendário é de janeiro a março de 2027, com temas que não batem com novembro.

## Próximos passos sugeridos

1. Você revisa as peças (pasta `producao/` e o `docs/calendario-2027-t1.md`).
2. Aprova ou ajusta os itens das pendências 1 a 7.
3. Eu gero as semanas 5 a 13 com o mesmo método, depois de aprovado o primeiro mês.
