# Como atualizar o repositório

<p align="center"><img src="../docs/assets/logo-unishare.png" alt="Logomarca UniShare" width="360"></p>

1. Faça backup do clone local e confirme `git status`. Se houver mudanças que não aparecem no ZIP de 25/11/2026, preserve-as e compare antes de substituir arquivos.
2. Extraia o pacote final em uma pasta separada. Copie o conteúdo da pasta `UniShare-corrigido` para a raiz do clone existente, sem substituir ou apagar `.git`.
3. Depois de conferir os novos documentos, remova os arquivos antigos indicados no guia de correções entregue junto ao ZIP. Os arquivos `a` são marcadores de pastas, não entregáveis; a pasta `wireframes/` antiga na raiz não é necessária.
4. Revise o README e navegue pelos links relativos. Confira as dez imagens em `prototipo/mockups/` e dez SVGs em `prototipo/wireframes/`. Não é necessário baixar as imagens separadamente.
5. Execute os comandos abaixo no PowerShell, na raiz do clone.

```powershell
git status
git add -A
git diff --cached --stat
```

Depois de conferir as mudanças:

```powershell
git commit -m "Consolida documentacao e modelagem P1 e P2 do UniShare"
git push origin main
```

Use a branch correta caso a principal não seja `main`. Não use push forçado. O histórico mantém os artefatos anteriores.

## Kanban e AVA

- Conferir as issues e milestones da turma e relacioná-las aos arquivos em [entregas P1/P2](entregas-p1-p2.md).
- Fechar somente as issues cujos critérios foram cumpridos; entrevista e dispensa de navegação não podem ser presumidas.
- Conferir acesso do professor `marcelobezerra-dotcom` ao repositório e entregar os links solicitados no AVA.
- As imagens estão em [prototipação](../prototipo/README.md); não há aplicação navegável neste pacote. Confirmar com o professor se prints são suficientes também para a entrega no AVA.
