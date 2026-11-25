# CDU-25 — Gerenciar Participantes da Turma

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Gerenciar Participantes da Turma

## 2. Objetivo

Autorizar ou recusar ingresso e gerenciar participantes de turmas próprias.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

AT-08 — Estudante cujo vínculo é decidido.

## 5. Precondições

Turma sob responsabilidade do ator; há pedido pendente no cenário principal. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor abre os participantes de uma turma própria.

**P2.** O sistema apresenta vínculos ativos e pedidos pendentes.

**P3.** O professor seleciona pedido e autoriza a participação.

**P4.** O sistema registra decisão, ativa o vínculo e atualiza as permissões de acesso à turma.

## 7. Fluxos Alternativos

**A1.** P3: Professor recusa pedido; o sistema registra recusa sem conceder acesso. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Professor remove participante com confirmação; o sistema revoga acesso futuro preservando registros conforme política. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Turma não pertence ao professor ou pedido já decidido: o sistema recusa mudança indevida. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Vínculo ativo, recusado ou revogado, com histórico.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-10, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Somente responsável autorizado decide ingresso; estudante aprovado pode consultar materiais.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-25.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-25.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
