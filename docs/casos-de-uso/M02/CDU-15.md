# CDU-15 — Manter Grupo de Estudo

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Grupo de Estudo

## 2. Objetivo

Criar e manter grupos de estudo e gerenciar participantes quando responsável.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Para manutenção, existe grupo sob responsabilidade do ator. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona criar grupo de estudo.

**P2.** O sistema apresenta campos de nome, tema, descrição e modalidade de ingresso.

**P3.** O usuário informa os dados e confirma.

**P4.** O sistema cria o grupo, registra o criador como responsável e apresenta o grupo.

## 7. Fluxos Alternativos

**A1.** P1: Responsável edita dados do grupo ou encerra o grupo após confirmação. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: Responsável consulta pedidos de ingresso e aceita ou recusa em grupo restrito; pode remover participantes segundo a política. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P3: Cancelamento não altera o grupo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Nome ou dados inválidos, falta de permissão ou falha de armazenamento: o sistema recusa a operação. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Grupo criado ou mantido, com participação controlada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Grupos de estudo](../../../prototipo/mockups/grupos.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Criador pode administrar seu grupo; participante comum não consegue aprovar pedidos de ingresso.

**Regras relacionadas:** [RN-05](../../requisitos/regras-de-negocio.md#rn-05)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-04 / F-15.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-15.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
