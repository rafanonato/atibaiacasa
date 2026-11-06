# Estratégia de engajamento e reservas: janeiro a março de 2027

Status: **proposta para aprovação**. Nada aqui foi executado. Publicação, anúncio com gasto e mudança no Airbnb só acontecem após aprovação explícita, caso a caso.

Data de referência: 2026-11-06.

## 1. Objetivo

Trazer reservas para o primeiro trimestre de 2027 (janeiro a março), com foco em fins de semana, Carnaval e a emenda de Sexta-feira Santa.

Hipótese central: a conta do Instagram está parada desde junho de 2024 e tem 199 seguidores. Por isso, o engajamento orgânico sozinho não vai mover as reservas no curto prazo. Propomos combinar três frentes: retomada orgânica com Reels, uso das avaliações reais do Airbnb como prova social e um teste pequeno de anúncio segmentado.

## 2. Diagnóstico (resumo dos dados)

| Fonte | O que mostra |
|---|---|
| Instagram (Windsor) | 199 seguidores, 10 posts, último em 17/06/2024. Alcance de 155 a 375 por post. Reels têm 812 a 1.127 visualizações; fotos quase nenhuma. |
| Público (Windsor) | 109 seguidores em São Paulo capital, 17 em Atibaia, 15 em Guarulhos, 6 em São Caetano do Sul e 6 em Santo André. Mulheres de 25 a 54 anos são a maior parte (cerca de 57% dos seguidores com faixa etária conhecida). |
| Airbnb | Nota 4,75 com 40 avaliações. Temas mais citados: hospitalidade, espaço, precisão, conforto, família e piscina. |
| Calendário 2027 | Preços e emendas aplicados. Carnaval (5 a 9/2) já tem uma reserva. Ano Novo (1/1) fica fora das alterações. |

Lacuna importante: não tenho a ocupação atual de janeiro a março. Sem ela não dá para saber quais datas estão vazias e precisam de empurrão. Próximo passo: exportar o calendário do Airbnb para essas datas.

## 3. Canais e papéis

| Canal | Papel | Quem executa |
|---|---|---|
| Airbnb | Vitrine de reserva; avaliações e fotos oficiais | Você (fotos e cadastro) |
| Instagram orgânico (@atibaiacasa) | Reels e carrosséis que levam ao Airbnb; stories para relacionamento | Eu escrevo e planejo; você aprova; publicação via Windsor |
| Meta Ads (a conectar) | Teste pequeno para São Paulo capital e Grande SP | Eu monto; você aprova o orçamento e cada campanha |
| WhatsApp | Conversão de quem pergunta | Você |

Link da bio: hoje aponta para a Keepo. Proposta: avaliar apontar para o Airbnb, já que é lá que estão as avaliações e o calendário.

## 4. Pilares de conteúdo

1. **A casa:** piscina, campo, área gourmet, suítes. Os Reels usam as fotos do Airbnb e textos curtos.
2. **Família e amigos:** cenas de uso (sem identificar pessoas sem autorização).
3. **Prova social:** trechos reais de avaliações do Airbnb, com autorização do hóspede quando possível.
4. **Datas e emendas:** Carnaval, Páscoa, Dia das Mulheres e férias de verão.
5. **Atibaia:** o que fazer na cidade, com informações verificadas antes de publicar.

## 5. Ritmo de publicação

- **Semanas 1 e 2 (retomada):** 2 Reels por semana e 2 stories.
- **A partir da semana 3:** 2 Reels e 1 carrossel por semana, mais 3 stories por semana.
- **Total no trimestre:** 26 Reels, 11 carrosséis e 37 stories.

Horários e dias serão definidos com base nos dados de alcance das primeiras semanas. Não há dado de horário do público no Windsor hoje.

## 6. Calendário semanal (janeiro a março de 2027)

Semana 1 começa em segunda, 4/1/2027.

### Janeiro: férias de verão em família

- **Semanas 1 e 2:** "Por dentro da casa" (Reel de tour com as fotos do Airbnb), "piscina e campo, o que você encontra" (Reel) e um Reel com o dado real de 4,75 de nota e 40 avaliações.
- **Semanas 3 e 4:** "Terça a quinta com flexibilidade" (Reel com a regra aprovada de entrada e saída). Depoimento de hóspede (quando houver autorização).
- **Semana 5:** início da campanha de Carnaval, com chamada para as datas de 5 a 9/2.

### Fevereiro: Carnaval

- **Semanas 6 e 7:** Reel "Carnaval em casa com a turma" e carrossel com o que levar e o que a casa oferece.
- **Semana 8 (Carnaval, 5 a 9/2):** stories ao vivo ou de bastidor, sem divulgar dados de hóspedes.
- **Semana 9:** pós-Carnaval, avaliação de quem esteve lá (com autorização) e chamada para a emenda de março.

### Março: Páscoa e Dia das Mulheres

- **Semana 10:** Reel "Escapada entre amigas" para o Dia das Mulheres (8/3, segunda-feira). Sugestão de conteúdo, não de promoção.
- **Semanas 11 e 12:** Sexta-feira Santa (25 a 28/3) e Páscoa. Carrossel com a emenda e o preço de R$ 1.400 com mínimo de 3 noites, como aprovado.
- **Semana 13:** fechamento do trimestre com resultados e planejamento do segundo trimestre.

Cada semana terá um texto, uma mídia e um CTA aprovados antes de publicar.

## 7. Produção de vídeo: análise da skill HyperFrames

Repositório: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes). Apache 2.0, cerca de 80 mil estrelas, atualizado em 06/11/2026.

**O que faz:** escreve vídeo em HTML e CSS e renderiza MP4 de forma determinística. Tem skills para Claude Code, incluindo `/hyperframes`, `/media-use` e `/hyperframes-registry` (cerca de 450 blocos prontos, como títulos, legendas e transições).

**Adequação ao nosso caso:**
- Bom para Reels de fotos: slideshow em 9:16, legendas, textos e movimento de câmera (zoom e deslocamento). É o formato que o Airbnb já fornece.
- Roda localmente, sem custo de API para renderizar.
- Requisitos: Node.js 22 ou superior e FFmpeg.
- O Studio gratuito serve para edição. O plano Pro adiciona modelos de vídeo, imagem, voz e música da HeyGen, pagos. Não precisamos deles para o plano inicial.
- Não faz avatar falando. Se quiser um avatar, é outro custo.

**Riscos e cuidados:**
- Skills são código que roda na sua máquina. Antes de instalar, revisar o que será executado. Recomendo instalar apenas o conjunto básico (`/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use`).
- Música: publicar via Windsor não adiciona áudio da biblioteca do Instagram. Usar música sem direitos pode bloquear o Reel. Precisamos definir a fonte de música antes.
- Mídia precisa de URL pública para o Windsor publicar (`video_url`). O repositório é privado, então não serve para hospedar os arquivos. Precisamos de outra forma de hospedagem pública.

**Recomendação:** usar o HyperFrames para os Reels de fotos. Instalar só depois da sua aprovação.

## 8. Alternativas encontradas

| Opção | Licença | Estado | Prós | Contras |
|---|---|---|---|---|
| [mahmadmanzoor/reel-studio](https://github.com/mahmadmanzoor/reel-studio) | MIT | Atualizado em 05/11/2026, 0 estrelas | Faz Reels com personagens e voz; movimento por código | Muito novo, sem histórico; voz depende de ElevenLabs (pago) |
| [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) | MIT | 5.099 estrelas, último push em 13/09/2026 | 13 skills, 26 fórmulas de gancho pontuadas, pesquisa de virais, revisor de legenda | Não gera vídeo. Concorre com as skills de escrita que já instalamos. Não auditei o código. |
| Pexo, Creatomate, outras APIs | Pagas | Serviços hospedados | Geram vídeo com modelos de IA | Custo por vídeo; dependência de API de terceiro |

**Para escrita:** as skills que já instalamos (`sergebulaev/instagram-skills`) cobrem o trabalho. A do Jakeschincariol pode complementar na pontuação de ganchos, mas só depois de auditoria, como fizemos com a primeira.

**Para vídeo:** HyperFrames é a melhor opção hoje para o nosso caso, por ser gratuito, local, com licença Apache e bem mantido.

## 9. Mídia paga (proposta, não aprovada)

- **Público:** São Paulo capital e Grande SP, mulheres de 25 a 54 anos, interesse em viagens e lazer. Atibaia como cidade de referência para quem mora na região.
- **Teste:** 2 semanas, orçamento a definir por você. Sugestão de partida: R$ 50 por dia, sem ultrapassar o total aprovado.
- **Critério de continuidade:** custo por mensagem no WhatsApp ou por clique no Airbnb, comparado com a taxa de conversão do Airbnb.
- **Pré-requisito:** conectar o Meta Ads no Windsor. Hoje a conta `facebook` não está conectada.

Nenhum gasto será feito sem sua confirmação de valor e de cada campanha.

## 10. Pré-requisitos antes de qualquer campanha

1. Confirmar a capacidade oficial (5 suítes e 20 pessoas, como indicado), e atualizar o cadastro e a Keepo. Campanha que atrai grupo com informação errada gera avaliação ruim.
2. Ajustar a taxa por pessoa extra para acima de 18 pessoas.
3. Resolver as regras de fumo e alarmes (detector de fumaça e de monóxido).
4. Obter a ocupação de janeiro a março no Airbnb.
5. Definir onde ficam as fotos e vídeos com URL pública para o Windsor.
6. Definir a fonte de música para os Reels.

## 11. Aprovações necessárias

- [ ] Calendário e temas de janeiro a março (seção 6)
- [ ] Ritmo de publicação (seção 5)
- [ ] Uso das fotos do Airbnb nos posts (confirmar que as pessoas que aparecem nas fotos consentiram)
- [ ] Instalar o HyperFrames e as skills básicas
- [ ] Mudar o link da bio do Keepo para o Airbnb
- [ ] Conectar o Meta Ads no Windsor
- [ ] Orçamento e duração do teste pago (seção 9)
- [ ] Pré-requisitos da seção 10 (capacidade, taxa, fumo e alarmes)

## 12. Métricas

| Métrica | Como medir | Referência atual |
|---|---|---|
| Seguidores | Windsor, `followers_count` | 199 |
| Alcance por post | Windsor, `media_reach` | 155 a 375 |
| Visualizações de Reels | Windsor, `media_views` | 812 a 1.127 |
| Cliques no link da bio | Windsor (campos de perfil) ou link rastreável | Não medido |
| Mensagens no WhatsApp | Contagem manual | Não medido |
| Reservas por trimestre | Airbnb | A definir após a ocupação atual |
| Ocupação de fins de semana | Airbnb | A definir |
| Novas avaliações | Airbnb | 40 hoje |

Revisão quinzenal. Ajustar temas e ritmo com base no alcance e nas mensagens.

## 13. Fontes

- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- [mahmadmanzoor/reel-studio](https://github.com/mahmadmanzoor/reel-studio)
- [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
- Dados da conta e do público: Windsor (conector `instagram`)
- Calendário e preços: `docs/02 - Preços e calendário 2027 (versão 05-11-2026).md`
- Anúncio: `docs/01 - Título e descrição do anúncio (aplicado 04-11-2026).md`
