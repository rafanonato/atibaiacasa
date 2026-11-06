# Registro de decisões

Cada decisão importante do projeto fica aqui, com data, motivo e o que muda por causa dela. Novas entradas vão no topo.

---

## 2026-11-06: Documentar decisões em `docs/decisoes.md`

- **Decisão:** toda decisão importante é registrada neste arquivo.
- **Motivo:** o contexto de uma conversa não persiste. O registro permite retomar o trabalho em outra sessão.
- **Impacto:** o `CLAUDE.md` da raiz manda registrar aqui cada decisão.

## 2026-11-06: Conexão com Instagram via Windsor

- **Decisão:** usar o conector Windsor (OAuth oficial da Meta) para ler a conta e publicar. Anúncios também via Windsor (Meta Ads, quando conectado).
- **Motivo:** OAuth oficial, sem cookies de sessão e sem terceiro guardando o token do Instagram.
- **Descartado:** instamcp (cookie de sessão, frágil); servidores MCP do GitHub que dependem de cookies.
- **Conta conectada:** @atibaiacasa (ID `17841452302392546`). Antes estava conectada outra conta (`setentapontomais`), substituída.

## 2026-11-06: Skills de conteúdo instaladas do `sergebulaev/instagram-skills`

- **Decisão:** instalar 8 skills de escrita em `.claude/skills/`: `ig-caption-writer`, `ig-carousel-planner`, `ig-content-planner`, `ig-hashtag-strategist`, `ig-hook-extractor`, `ig-humanizer`, `ig-profile-optimizer`, `ig-repurposer`. Referências compartilhadas em `.claude/references/`.
- **Motivo:** cobrem o trabalho de conteúdo (legendas, ganchos, carrossel, plano semanal, hashtags, perfil). A publicação fica com o Windsor.
- **Não instalado:** `ig-audience-insights`, porque depende do Apify e faz scraping de conta pública.
- **Pendência:** as skills ainda citam Publora na publicação. Sem `PUBLORA_API_KEY`, elas devolvem o texto para postar no app. Não foram testadas rodando.

## 2026-11-06: Publora, Apify e Pixfaro não configurados

- **Decisão:** não usar Publora (publicação de terceiros), Apify (scraping) nem Pixfaro (imagens pagas) por enquanto.
- **Motivo:** evitar terceiros com acesso ao token do Instagram e uma fonte de dados em zona cinzenta. O Windsor cobre a publicação.
- **Reavaliar se:** o Windsor não atender algum caso de uso.

## 2026-11-06: Confirmação humana antes de publicar ou gastar

- **Decisão:** nenhuma publicação nem ação de anúncio com gasto sem confirmação explícita da pessoa, caso a caso.
- **Motivo:** a conta gera receita de reservas. Um erro de post ou de orçamento custa caro.
- **Como aplicar:** mostrar o rascunho completo (legenda, mídia, horário) e esperar um "sim".

## 2026-11-06: Repositório privado e credenciais

- **Decisão:** repositório privado em `github.com/rafanonato/atibaiacasa`, branch `main`.
- **Credencial:** `gh auth setup-git` configurado globalmente, para o Git usar o `gh` em `github.com`.
- **Arquivos ignorados:** `.env` e variantes (chaves de API ficam só na máquina).

## 2026-11-06: Conta da @atibaiacasa como referência de estado

- **Decisão:** o resumo da conta e do negócio fica em `docs/atibaiacasa.md`.
- **Pendências:** preço, endereço, check-in, avaliações e canais de reserva ainda não foram confirmados.
