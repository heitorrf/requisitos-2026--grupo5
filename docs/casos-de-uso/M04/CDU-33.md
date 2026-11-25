# CDU-33 — Acompanhar Desempenho da Turma

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Acompanhar Desempenho da Turma

## 2. Objetivo

Consultar resultados individuais e coletivos de turmas próprias.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Turma sob responsabilidade do professor. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor abre desempenho de turma própria.

**P2.** O sistema verifica responsabilidade e apresenta lista de atividades, entregas e avaliações.

**P3.** O professor seleciona uma atividade ou estudante.

**P4.** O sistema apresenta os resultados autorizados e resumo de entregas e notas disponíveis, distinguindo ausência de nota.

## 7. Fluxos Alternativos

**A1.** P3: Professor consulta visão coletiva com contagem de entregas e média apenas das notas registradas. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Sem avaliações, o sistema mostra ausência de dados, não média zero. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Professor de outra turma não recebe os dados. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhuma avaliação alterada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-10. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Notas e desempenho](../../../prototipo/mockups/notas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Resumo coletivo usa somente turma própria e exclui notas não registradas do cálculo da média.

**Regras relacionadas:** [RN-07](../../requisitos/regras-de-negocio.md#rn-07), [RN-08](../../requisitos/regras-de-negocio.md#rn-08), [RN-16](../../requisitos/regras-de-negocio.md#rn-16)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-08 / F-33.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-33.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
