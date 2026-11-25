# CDU-29 — Consultar Atividades

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Atividades

## 2. Objetivo

Acessar orientações, prazos e situação das atividades.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante, AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Vínculo ativo com turma ou responsabilidade docente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário abre atividades de turma acessível.

**P2.** O sistema valida vínculo e apresenta atividades com prazo e estado.

**P3.** O usuário seleciona atividade.

**P4.** O sistema apresenta instruções e estado da entrega própria, ou visão de gestão para professor responsável.

## 7. Fluxos Alternativos

**A1.** P2: Usuário filtra por pendentes, entregues ou encerradas. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Se não houver atividade, o sistema informa lista vazia. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Atividade removida ou acesso revogado: o sistema recusa detalhes restritos. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhuma atividade ou entrega alterada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-10. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Atividades e entregas](../../../prototipo/mockups/atividades.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Estudante visualiza apenas o estado de sua própria entrega; professor acessa as informações de gestão da turma.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06), [RN-07](../../requisitos/regras-de-negocio.md#rn-07), [RN-15](../../requisitos/regras-de-negocio.md#rn-15)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-29.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-29.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
