# CDU-23 — Consultar Turmas

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Turmas

## 2. Objetivo

Visualizar turmas acessíveis e respectivos dados.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante, AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Não se aplica. As permissões gerais são verificadas pelo sistema quando a operação exigir acesso restrito.

## 6. Fluxo Principal

**P1.** O usuário abre turmas.

**P2.** O sistema apresenta turmas próprias para professor ou turmas disponíveis e vínculos para estudante.

**P3.** O usuário seleciona uma turma.

**P4.** O sistema apresenta somente informações públicas ou informações da turma autorizadas para seu vínculo.

## 7. Fluxos Alternativos

**A1.** P3: Estudante sem vínculo visualiza informações de ingresso, não materiais e notas. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Se não houver turmas, apresenta estado vazio. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Acesso direto indevido a turma restrita: o sistema recusa os dados privados. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhum vínculo criado pela consulta.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-10. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Estudante não inscrito não visualiza materiais privados; professor vê suas turmas.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-23.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-23.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
