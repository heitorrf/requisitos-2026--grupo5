# CDU-31 — Avaliar Entregas

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Avaliar Entregas

## 2. Objetivo

Avaliar entregas, atribuir notas dentro da escala da atividade e atualizar feedback.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Entrega existente em turma sob responsabilidade do ator. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor abre entregas de atividade de turma própria.

**P2.** O sistema verifica responsabilidade e lista entregas autorizadas.

**P3.** O professor seleciona entrega, informa nota e feedback e confirma.

**P4.** O sistema valida faixa de pontuação, grava a avaliação e disponibiliza somente ao estudante avaliado.

## 7. Fluxos Alternativos

**A1.** P3: Professor atualiza nota ou feedback já registrado e informa justificativa; o sistema mantém histórico da alteração. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Sem entregas, o sistema apresenta lista vazia. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Nota fora da faixa, professor sem autorização ou falha de gravação: o sistema não altera a avaliação. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Avaliação registrada ou atualizada; estudante pode consultar a própria.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-05, RNF-08, RNF-10, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Atividades e entregas](../../../prototipo/mockups/atividades.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Nota superior à pontuação máxima é rejeitada; avaliação válida aparece apenas para o aluno avaliado e professor responsável.

**Regras relacionadas:** [RN-07](../../requisitos/regras-de-negocio.md#rn-07), [RN-08](../../requisitos/regras-de-negocio.md#rn-08), [RN-16](../../requisitos/regras-de-negocio.md#rn-16)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-08 / F-31.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-31.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
