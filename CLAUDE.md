# Projeto atibaiacasa

Gestão integrada do Instagram da @atibaiacasa (Casa Atibaia): captação de conteúdo, escrita, aprovação e publicação, com foco em aumentar visibilidade e reservas para o próximo ano.

## Convenções

- **Registre decisões importantes em `docs/decisoes.md`**, no topo, com data, decisão, motivo e impacto. Faça isso sem precisar que peçam.
- Resumo do negócio e da conta fica em `docs/atibaiacasa.md`. Atualize quando algum dado mudar.
- Skills de conteúdo ficam em `.claude/skills/`, com referências compartilhadas em `.claude/references/`.
- `voice-profile.md` em `.claude/references/` precisa ser preenchido antes de escrever legendas.
- Não publicar nem gastar em anúncio sem confirmação explícita da pessoa, caso a caso.
- Nunca commitar `.env` nem chaves de API.
- Commits: mensagem em português, com a linha `Co-Authored-By` do Claude.
- Publicação e leitura da conta: via conector Windsor (`instagram`, e `facebook` para Meta Ads quando conectado).

## Produção de peças

- Fonte única: `producao/scripts/pecas.py` (textos, legendas, fotos, datas). Altere só ali e rode os scripts.
- Scripts em `producao/scripts/`: `build_graficos.py` (imagens), `build_reels.py` (projetos HyperFrames), `gerar_calendario.py` (calendário), `validar.py` (checagem). Use `producao/.venv/bin/python`.
- Renders MP4 e `.hyperframes/` não vão para o Git. Regenere com `npx hyperframes@0.9.19 render` dentro de cada `producao/reels/<id>`.
- Fotos originais: `docs/Fotos do anúncio Airbnb/`. Peças derivadas ficam em `producao/`.
- Validação e pendências do primeiro mês: `docs/validacao-pecas-primeiro-mes.md`.
- Skills de vídeo (HyperFrames) instaladas em `.agents/skills/` e linkadas em `.claude/skills/`.

## Estado atual

Ver `docs/atibaiacasa.md` e `docs/decisoes.md`.
