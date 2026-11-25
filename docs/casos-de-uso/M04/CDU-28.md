# CDU-28 — Manter Atividade

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Atividade

## 2. Objetivo

Criar, atualizar e encerrar tarefas, exercícios e avaliações com prazo.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Turma ativa sob responsabilidade do ator. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor abre atividades de turma própria.

**P2.** O sistema apresenta campos de título, instruções, prazo, pontuação máxima e forma de entrega.

**P3.** O professor preenche e confirma.

**P4.** O sistema valida prazo, pontuação e autorização, grava e publica a atividade.

## 7. Fluxos Alternativos

**A1.** P1: Professor edita atividade própria; o sistema preserva entregas existentes e registra mudanças de prazo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: Professor encerra atividade; o sistema bloqueia novas entregas. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P3: Cancelamento não altera atividade. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Prazo inválido, pontuação não positiva ou erro de armazenamento: o sistema não publica a atividade. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Atividade publicada, atualizada ou encerrada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-05, RNF-08, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Atividades e entregas](../../../prototipo/mockups/atividades.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Atividade com prazo e pontuação válidos é visível aos participantes; encerrada não aceita novas entregas.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06), [RN-15](../../requisitos/regras-de-negocio.md#rn-15), [RN-16](../../requisitos/regras-de-negocio.md#rn-16)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-28.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-28.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
