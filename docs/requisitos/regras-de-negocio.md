# Regras de Negócio — UniShare

<p align="center"><img src="../assets/logo-unishare.png" alt="Logomarca UniShare" width="360"></p>

**Grupo 5 · Versão 1.0 · 25/11/2026**

> Proposta acadêmica para revisão; não representa validação por usuários reais.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## Especificação

Regras de negócio propostas com base na visão inicial e nas decisões de modelagem. Não são normas institucionais validadas. Cada seção contém condição, resultado esperado e teste de aceitação.

### RN-01

**A plataforma restringe a concessão de perfis.**

**Descrição:** No cadastro público, o visitante escolhe estudante local, intercambista ou candidato a professor; o perfil administrativo é concedido por procedimento operacional restrito.

**Verificação:** Uma conta comum não consegue conceder perfil administrativo.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-01](../casos-de-uso/M01/CDU-01.md), [CDU-05](../casos-de-uso/M01/CDU-05.md), [CDU-07](../casos-de-uso/M01/CDU-07.md), [CDU-38](../casos-de-uso/M06/CDU-38.md), [CDU-39](../casos-de-uso/M06/CDU-39.md)

### RN-02

**A administração autoriza o perfil docente.**

**Descrição:** Quando um estudante ou candidato solicita perfil docente, somente administrador autorizado decide após examinar comprovação. Enquanto pendente, o usuário não recebe funções docentes; ao aprovar, o perfil docente torna-se efetivo, sem apagar registros acadêmicos anteriores. Critérios documentais ainda devem ser validados.

**Verificação:** Pedido pendente não permite criar turma; aprovação permite.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-07](../casos-de-uso/M01/CDU-07.md), [CDU-22](../casos-de-uso/M04/CDU-22.md), [CDU-39](../casos-de-uso/M06/CDU-39.md)

### RN-03

**O destinatário aceita a conexão.**

**Descrição:** Uma conexão só é criada após aceitação do destinatário; novas mensagens diretas exigem conexão ativa e ausência de bloqueio.

**Verificação:** Pedido pendente não permite nova mensagem; pedido aceito permite.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-10](../casos-de-uso/M02/CDU-10.md), [CDU-11](../casos-de-uso/M02/CDU-11.md), [CDU-44](../casos-de-uso/M06/CDU-44.md)

### RN-04

**O autor mantém suas publicações.**

**Descrição:** Somente o autor edita ou exclui publicações e comentários próprios; retirada por moderação constitui ação separada, justificada e registrada.

**Verificação:** Conta de terceiro não consegue editar publicação alheia.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-13](../casos-de-uso/M02/CDU-13.md), [CDU-14](../casos-de-uso/M02/CDU-14.md), [CDU-43](../casos-de-uso/M06/CDU-43.md)

### RN-05

**O responsável administra o grupo.**

**Descrição:** O criador ou responsável autorizado gerencia dados e membros do grupo. Grupo aberto admite ingresso direto; grupo restrito exige aprovação do responsável; grupo encerrado não admite novos membros.

**Verificação:** Pedido pendente não libera conteúdo restrito.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-12](../casos-de-uso/M02/CDU-12.md), [CDU-13](../casos-de-uso/M02/CDU-13.md), [CDU-15](../casos-de-uso/M02/CDU-15.md), [CDU-16](../casos-de-uso/M02/CDU-16.md), [CDU-17](../casos-de-uso/M02/CDU-17.md)

### RN-06

**O professor responsável autoriza o ingresso.**

**Descrição:** O estudante só acessa materiais, atividades e comunicados privados quando possui vínculo ativo com a turma; somente professor responsável autoriza ou revoga participação.

**Verificação:** Usuário sem vínculo não obtém material por acesso direto.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-22](../casos-de-uso/M04/CDU-22.md), [CDU-23](../casos-de-uso/M04/CDU-23.md), [CDU-24](../casos-de-uso/M04/CDU-24.md), [CDU-25](../casos-de-uso/M04/CDU-25.md), [CDU-26](../casos-de-uso/M04/CDU-26.md), [CDU-27](../casos-de-uso/M04/CDU-27.md), [CDU-28](../casos-de-uso/M04/CDU-28.md), [CDU-29](../casos-de-uso/M04/CDU-29.md), [CDU-30](../casos-de-uso/M04/CDU-30.md), [CDU-34](../casos-de-uso/M04/CDU-34.md), [CDU-35](../casos-de-uso/M04/CDU-35.md)

### RN-07

**A plataforma restringe resultados acadêmicos.**

**Descrição:** Estudante consulta suas próprias entregas, notas e feedback; professor consulta os resultados das turmas sob sua responsabilidade.

**Verificação:** Estudante A não obtém a nota de B.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-29](../casos-de-uso/M04/CDU-29.md), [CDU-30](../casos-de-uso/M04/CDU-30.md), [CDU-31](../casos-de-uso/M04/CDU-31.md), [CDU-32](../casos-de-uso/M04/CDU-32.md), [CDU-33](../casos-de-uso/M04/CDU-33.md)

### RN-08

**O UniShare mantém notas internas.**

**Descrição:** Notas são registros internos da plataforma; não equivalem a notas oficiais, matrícula ou histórico institucional.

**Verificação:** Interface de desempenho identifica resultados internos.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-31](../casos-de-uso/M04/CDU-31.md), [CDU-32](../casos-de-uso/M04/CDU-32.md), [CDU-33](../casos-de-uso/M04/CDU-33.md)

### RN-09

**A tradução preserva o original.**

**Descrição:** A tradução é sob demanda, apenas de texto acessível e elegível; original não é sobrescrito. Em falha, continua legível.

**Verificação:** Falha no serviço mantém o texto original.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-37](../casos-de-uso/M05/CDU-37.md)

### RN-10

**O sistema recomenda conteúdo por afinidade.**

**Descrição:** Recomendações consideram áreas, interesses e referências ativas; sem dados suficientes, apresenta sugestões gerais ou lista vazia.

**Verificação:** Perfis de áreas diferentes recebem referências coerentes.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-05](../casos-de-uso/M01/CDU-05.md), [CDU-21](../casos-de-uso/M03/CDU-21.md), [CDU-41](../casos-de-uso/M06/CDU-41.md)

### RN-11

**O responsável mantém os conteúdos de descoberta.**

**Descrição:** Professores mantêm apenas divulgações próprias; administradores mantêm locais, orientações e catálogos de apoio. Itens retirados não aparecem na consulta padrão.

**Verificação:** Item inativo não é apresentado como recomendação ativa.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-18](../casos-de-uso/M03/CDU-18.md), [CDU-19](../casos-de-uso/M03/CDU-19.md), [CDU-20](../casos-de-uso/M03/CDU-20.md), [CDU-21](../casos-de-uso/M03/CDU-21.md), [CDU-40](../casos-de-uso/M06/CDU-40.md), [CDU-41](../casos-de-uso/M06/CDU-41.md)

### RN-12

**A administração registra ações sensíveis.**

**Descrição:** Concessão de perfil, suspensão, moderação e exclusão exigem autorização e registro de ator, instante, motivo e resultado. Não há acesso administrativo irrestrito a notas ou conversas.

**Verificação:** Administrador visualiza apenas evidência autorizada e registra medida.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-38](../casos-de-uso/M06/CDU-38.md), [CDU-39](../casos-de-uso/M06/CDU-39.md), [CDU-43](../casos-de-uso/M06/CDU-43.md), [CDU-45](../casos-de-uso/M06/CDU-45.md)

### RN-13

**A plataforma confirma a posse do e-mail.**

**Descrição:** Confirmação e recuperação utilizam tokens de uso único e temporários; posse de e-mail não comprova vínculo docente. Conta não confirmada não inicia sessão.

**Verificação:** Token expirado não confirma conta nem altera senha.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-01](../casos-de-uso/M01/CDU-01.md), [CDU-02](../casos-de-uso/M01/CDU-02.md), [CDU-03](../casos-de-uso/M01/CDU-03.md), [CDU-07](../casos-de-uso/M01/CDU-07.md)

### RN-14

**A plataforma trata pedidos de exclusão.**

**Descrição:** Após solicitação confirmada, exclusão ou anonimização respeita retenção justificada e direitos de terceiros; conta é encerrada somente no processamento autorizado. A política de retenção deve ser aprovada antes de uso real.

**Verificação:** Sem política aplicável, pedido não aparece como concluído.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-08](../casos-de-uso/M01/CDU-08.md), [CDU-45](../casos-de-uso/M06/CDU-45.md)

### RN-15

**A atividade define o prazo de entrega.**

**Descrição:** Uma atividade possui prazo e pontuação máxima positiva; somente turma ativa e atividade aberta aceitam entrega até o prazo. Substituição, se habilitada, mantém versões anteriores.

**Verificação:** Entrega após prazo ou encerramento é recusada.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-22](../casos-de-uso/M04/CDU-22.md), [CDU-28](../casos-de-uso/M04/CDU-28.md), [CDU-29](../casos-de-uso/M04/CDU-29.md), [CDU-30](../casos-de-uso/M04/CDU-30.md)

### RN-16

**A avaliação respeita a pontuação da atividade.**

**Descrição:** A nota registrada pertence ao intervalo de zero à pontuação máxima. Atualização exige justificativa; ausência de nota não equivale a zero. Média coletiva considera apenas notas registradas.

**Verificação:** Nota acima do máximo é recusada; média exclui itens sem nota.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-28](../casos-de-uso/M04/CDU-28.md), [CDU-31](../casos-de-uso/M04/CDU-31.md), [CDU-32](../casos-de-uso/M04/CDU-32.md), [CDU-33](../casos-de-uso/M04/CDU-33.md)

### RN-17

**O bloqueio encerra interações diretas.**

**Descrição:** Bloqueio encerra conexão ativa e pedidos pendentes e impede novas mensagens ou solicitações diretas entre os envolvidos. Histórico previamente autorizado não é apagado; desbloqueio não restaura conexão automaticamente.

**Verificação:** Após desbloquear, nova conexão exige nova aceitação.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-06](../casos-de-uso/M01/CDU-06.md), [CDU-09](../casos-de-uso/M02/CDU-09.md), [CDU-10](../casos-de-uso/M02/CDU-10.md), [CDU-11](../casos-de-uso/M02/CDU-11.md), [CDU-44](../casos-de-uso/M06/CDU-44.md)

### RN-18

**O denunciante referencia conteúdo acessível.**

**Descrição:** Denúncia registra motivo e evidência acessível ao denunciante; administrador trata apenas dados necessários e identidade do denunciante não é exibida ao denunciado.

**Verificação:** Denúncia de conteúdo inacessível é recusada.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-42](../casos-de-uso/M06/CDU-42.md), [CDU-43](../casos-de-uso/M06/CDU-43.md)

### RN-19

**O usuário controla a visibilidade do perfil.**

**Descrição:** Dados opcionais respeitam configuração de visibilidade; e-mail e dados acadêmicos privados não são publicados por padrão.

**Verificação:** Consulta de outro perfil omite e-mail privado.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-05](../casos-de-uso/M01/CDU-05.md), [CDU-06](../casos-de-uso/M01/CDU-06.md), [CDU-09](../casos-de-uso/M02/CDU-09.md)

### RN-20

**O sistema restringe arquivos compartilhados.**

**Descrição:** Anexos só são aceitos nos formatos e limites definidos nos RNFs; consulta e download respeitam a mesma autorização do conteúdo.

**Verificação:** Arquivo acima do limite ou de formato não permitido é recusado.

**Origem:** Documento de Visão 4.0 / decisão de modelagem proposta.

**Casos relacionados:** [CDU-13](../casos-de-uso/M02/CDU-13.md), [CDU-26](../casos-de-uso/M04/CDU-26.md), [CDU-27](../casos-de-uso/M04/CDU-27.md), [CDU-30](../casos-de-uso/M04/CDU-30.md)

## Checklist de validação

- [x] IDs únicos, nome sujeito + verbo + objeto e condições explícitas.
- [x] Resultado verificável e referências aos CDUs.
- [ ] Revisão por pares e validação de políticas com usuários/administrador.
