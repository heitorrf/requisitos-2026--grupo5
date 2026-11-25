# CDU-24 — Solicitar Participação em Turma

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Solicitar Participação em Turma

## 2. Objetivo

Solicitar ingresso em turma ou cancelar pedido pendente.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante

### 4.2 Secundário

AT-03 — Professor responsável, recebe pedido; decisão no CDU-25.

## 5. Precondições

Turma existente e aberta para ingresso. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O estudante seleciona uma turma aberta a ingressos ou informa convite.

**P2.** O sistema apresenta dados da turma e verifica elegibilidade.

**P3.** O estudante confirma a solicitação.

**P4.** O sistema registra pedido pendente e informa que aguarda decisão do professor.

## 7. Fluxos Alternativos

**A1.** P1: Estudante com vínculo existente consulta seu estado sem gerar novo pedido. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Estudante cancela antes de confirmar; não cria solicitação. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P1: Estudante cancela pedido ainda pendente; o sistema encerra o pedido. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Turma encerrada, convite inválido ou pedido duplicado: o sistema não registra novo pedido. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Pedido pendente sem acesso privado até aprovação.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Solicitar ingresso não libera materiais; autorização depende do CDU-25.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-24.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-24.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
