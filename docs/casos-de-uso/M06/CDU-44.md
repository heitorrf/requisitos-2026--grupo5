# CDU-44 — Bloquear Usuário

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Bloquear Usuário

## 2. Objetivo

Bloquear usuário, encerrar conexão e impedir novas interações diretas; desfazer bloqueio.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Outro perfil existente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário abre perfil ou conversa de outro usuário.

**P2.** O sistema apresenta opção de bloqueio.

**P3.** O usuário seleciona bloquear e confirma.

**P4.** O sistema registra bloqueio e impede novos pedidos de conexão e mensagens diretas entre os dois perfis.

## 7. Fluxos Alternativos

**A1.** P1: Usuário abre lista de bloqueios e remove um bloqueio; o sistema permite novas solicitações conforme demais regras, sem restaurar conexão automaticamente. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Cancelamento não altera restrições. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Bloqueio inválido, como o próprio usuário, ou falha de gravação: o sistema recusa a operação. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Bloqueio ativo ou removido; conexões anteriores encerradas na ativação.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Mensagens](../../../prototipo/mockups/mensagens.png) · [Perfil acadêmico](../../../prototipo/mockups/perfil.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Usuário bloqueado não pode enviar novas mensagens; desbloquear não reativa vínculo automaticamente.

**Regras relacionadas:** [RN-03](../../requisitos/regras-de-negocio.md#rn-03), [RN-17](../../requisitos/regras-de-negocio.md#rn-17)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-44.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-44.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
