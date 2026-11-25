# CDU-08 — Solicitar Exclusão de Conta

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Solicitar Exclusão de Conta

## 2. Objetivo

Solicitar encerramento da conta e tratamento dos dados conforme política aplicável.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Conta existente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona excluir conta.

**P2.** O sistema explica consequências e dados sujeitos a retenção e solicita confirmação.

**P3.** O usuário confirma a identidade e a solicitação.

**P4.** O sistema registra pedido pendente e informa o acompanhamento.

## 7. Fluxos Alternativos

**A1.** P3: O usuário cancela; a conta permanece sem pedido. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: Pedido existente: o sistema informa o estado e não duplica a solicitação. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P3: Verificação de identidade inválida: o sistema recusa o pedido. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Pedido de exclusão registrado, sem apagar dados imediatamente.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Baixa — estimativa a validar.

## 13. Interface Visual

Referência visual: [Perfil acadêmico](../../../prototipo/mockups/perfil.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Cancelar não altera a conta; confirmar gera pedido rastreável para CDU-45.

**Regras relacionadas:** [RN-14](../../requisitos/regras-de-negocio.md#rn-14)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-08.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-08.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
