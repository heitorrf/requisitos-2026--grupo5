# CDU-19 — Consultar Eventos e Oportunidades

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M03 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Eventos e Oportunidades

## 2. Objetivo

Pesquisar palestras, workshops, congressos, vagas e oportunidades.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Não se aplica. As permissões gerais são verificadas pelo sistema quando a operação exigir acesso restrito.

## 6. Fluxo Principal

**P1.** O usuário abre eventos e oportunidades.

**P2.** O sistema apresenta filtros de área, data, categoria e modalidade.

**P3.** O usuário seleciona critérios e pesquisa.

**P4.** O sistema apresenta divulgações acessíveis com título, descrição, prazo e referência quando informados.

## 7. Fluxos Alternativos

**A1.** P3: O usuário inclui oportunidades encerradas para consulta, quando disponíveis. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P4: Seleciona um evento e visualiza os detalhes. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Falha na consulta: o sistema informa e permite nova tentativa. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhuma divulgação alterada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-12, RNF-20. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Explorar e descobrir](../../../prototipo/mockups/explorar.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Filtro de oportunidades abertas não inclui prazos encerrados; detalhes indicam a fonte fornecida.

**Regras relacionadas:** [RN-11](../../requisitos/regras-de-negocio.md#rn-11)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-05 / F-19.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-19.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M03](../../../diagramas-uml/casos-de-uso/M03.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
