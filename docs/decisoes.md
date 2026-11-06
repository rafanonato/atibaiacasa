# Registro de decisões

Cada decisão importante do projeto fica aqui, com data, motivo e o que muda por causa dela. Novas entradas vão no topo.

---

## Pendências após revisão de 05/11/2026

- **Capacidade (a confirmar):** Rafael indicou considerar 5 suítes e até 20 pessoas. O cadastro estruturado do Airbnb ainda diz 4 quartos e 16 camas. Mudar o cadastro exige aprovação separada (`docs/01 - ...`, seção 5). A Keepo ainda diz 16 hóspedes e 4 suítes, e precisa ser atualizada junto.
- **Fumo e alarmes (adiado por decisão de Rafael):** as regras mostram "Smoking allowed" e "No smoke alarm", e não há detector de fumaça ou de monóxido listado. Rafael decidiu não fazer esse ajuste agora. Fica registrado como risco de segurança do hóspede a ser resolvido.

## 2026-11-05: Taxa por pessoa extra acima de 18 pessoas

- **Decisão (Rafael):** a taxa adicional por pessoa passa a valer acima de 18 pessoas dormindo na casa, conforme o texto publicado.
- **Situação:** a configuração ainda está em R$ 0 após 15 hóspedes. Precisa ser ajustada no Airbnb para bater com o texto.
- **Motivo:** o texto do anúncio e a configuração de taxa não podem divergir.

## 2026-11-05: Consulta de grupo grande (Maria Carolina, 11 a 13/12/2026)

- **Situação:** pedido de cerca de 30 pessoas. Rafael já respondeu à cliente. Resposta não registrada aqui.
- **Por que registrar:** a resposta define um precedente de grupo grande para as próximas consultas. Vale anotar o valor combinado quando souber.

## 2026-11-05: Taxa efetiva do Airbnb verificada

- **Situação:** taxa efetiva de cerca de 18,21% do subtotal das noites. Rafael confirmou que está correta, após verificação.
- **Impacto:** nenhuma mudança de taxa ou classificação é necessária por enquanto.

## 2026-11-05: Calendário 2027 e taxa extra aplicados no Airbnb

- **Decisão (aprovada por Rafael):** não bloquear datas, só configurar preço e mínimo de noites. Reservas existentes em 2027 ficam intactas (Samanta 5 a 9/02, Letícia, Marcos).
- **Emendas de feriado 2027:** R$ 1.400 por noite, mínimo 3 noites. Carnaval, Sexta Santa, Corpus Christi, Aniversário de Atibaia, Revolução, Independência, Aparecida, Finados e República.
- **Fora das emendas:** sexta e sábado R$ 1.250 (jan a jun e ago a nov), R$ 1.350 em julho e de 1/12 até o Natal. Demais noites R$ 1.100, ou R$ 1.150 em julho e R$ 1.250 em dezembro. Mínimo de 2 noites.
- **Natal (23 a 25/12) e Ano Novo (28/12 a 2/1/2028):** R$ 2.000 por noite, mínimo 3. 26 e 27/12: R$ 1.250.
- **Virada 2026/27:** fica fora das alterações, por decisão de Rafael (05/11, 14:35).
- **Entrada e saída:** flexibilizadas para terça e quinta. Sexta a domingo mantém mínimo de 2 noites.
- **Taxa por pessoa extra:** R$ 0 após 15 hóspedes, por noite (antes R$ 100). Aplicada às 16:08 de 05/11. Substituída pela decisão de cobrar acima de 18 pessoas (acima).
- **stays.net:** removida às 15:49 de 05/11.
- **Motivo:** calendário e preços de 2027 para aumentar reservas com emendas e alta temporada.

## 2026-11-04: Título e descrição do anúncio Airbnb atualizados

- **Decisão (aprovada por Rafael):** título "Casa 5 suítes, piscina e campo @atibaiacasa" e descrição v5, com 5 suítes e até 20 pessoas para dormir. Fotos ficam com Rafael.
- **Motivo:** o texto anterior falava em 4 suítes e 16 pessoas, e o novo título traz o handle do Instagram.
- **Detalhes e texto anterior para reverter:** `docs/01 - Título e descrição do anúncio (aplicado 04-11-2026).md`.

## 2026-11-06: Airbnb identificado como canal de reserva ativo

- **Decisão:** o anúncio do Airbnb (ID `1131161848484082328`) é a casa da @atibaiacasa. Ele é a principal fonte de prova social (nota 4,75, 40 avaliações).
- **Motivo:** o nome do anúncio cita o @atibaiacasa, e o endereço e as características batem com a página da Keepo.
- **Impacto:** avaliações e temas de hóspedes passam a ser fonte para os textos do Instagram.

## 2026-11-06: Conta da @atibaiacasa como referência de estado

- **Decisão:** o resumo da conta e do negócio fica em `docs/atibaiacasa.md`.
- **Pendências:** preço, endereço, check-in, avaliações e canais de reserva ainda não foram confirmados.

## 2026-11-06: Repositório privado e credenciais

- **Decisão:** repositório privado em `github.com/rafanonato/atibaiacasa`, branch `main`.
- **Credencial:** `gh auth setup-git` configurado globalmente, para o Git usar o `gh` em `github.com`.
- **Arquivos ignorados:** `.env` e variantes (chaves de API ficam só na máquina).

## 2026-11-06: Confirmação humana antes de publicar ou gastar

- **Decisão:** nenhuma publicação nem ação de anúncio com gasto sem confirmação explícita da pessoa, caso a caso.
- **Motivo:** a conta gera receita de reservas. Um erro de post ou de orçamento custa caro.
- **Como aplicar:** mostrar o rascunho completo (legenda, mídia, horário) e esperar um "sim".

## 2026-11-06: Publora, Apify e Pixfaro não configurados

- **Decisão:** não usar Publora (publicação de terceiros), Apify (scraping) nem Pixfaro (imagens pagas) por enquanto.
- **Motivo:** evitar terceiros com acesso ao token do Instagram e uma fonte de dados em zona cinzenta. O Windsor cobre a publicação.
- **Reavaliar se:** o Windsor não atender algum caso de uso.

## 2026-11-06: Skills de conteúdo instaladas do `sergebulaev/instagram-skills`

- **Decisão:** instalar 8 skills de escrita em `.claude/skills/`: `ig-caption-writer`, `ig-carousel-planner`, `ig-content-planner`, `ig-hashtag-strategist`, `ig-hook-extractor`, `ig-humanizer`, `ig-profile-optimizer`, `ig-repurposer`. Referências compartilhadas em `.claude/references/`.
- **Motivo:** cobrem o trabalho de conteúdo (legendas, ganchos, carrossel, plano semanal, hashtags, perfil). A publicação fica com o Windsor.
- **Não instalado:** `ig-audience-insights`, porque depende do Apify e faz scraping de conta pública.
- **Pendência:** as skills ainda citam Publora na publicação. Sem `PUBLORA_API_KEY`, elas devolvem o texto para postar no app. Não foram testadas rodando.

## 2026-11-06: Conexão com Instagram via Windsor

- **Decisão:** usar o conector Windsor (OAuth oficial da Meta) para ler a conta e publicar. Anúncios também via Windsor (Meta Ads, quando conectado).
- **Motivo:** OAuth oficial, sem cookies de sessão e sem terceiro guardando o token do Instagram.
- **Descartado:** instamcp (cookie de sessão, frágil); servidores MCP do GitHub que dependem de cookies.
- **Conta conectada:** @atibaiacasa (ID `17841452302392546`). Antes estava conectada outra conta (`setentapontomais`), substituída.

## 2026-11-06: Documentar decisões em `docs/decisoes.md`

- **Decisão:** toda decisão importante é registrada neste arquivo.
- **Motivo:** o contexto de uma conversa não persiste. O registro permite retomar o trabalho em outra sessão.
- **Impacto:** o `CLAUDE.md` da raiz manda registrar aqui cada decisão.
