# CDU-18 — Consultar Locais Recomendados

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M03 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Locais Recomendados

## 2. Objetivo

Consultar guia de adaptação, orientações, locais de estudo, convivência, serviços e pontos turísticos.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Catálogo pode estar vazio. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário abre o guia de adaptação.

**P2.** O sistema apresenta categorias de locais, serviços do campus, convivência, pontos turísticos e orientações.

**P3.** O usuário filtra por categoria ou instituição e seleciona um item.

**P4.** O sistema apresenta descrição, referência de localização e data de atualização quando disponíveis.

## 7. Fluxos Alternativos

**A1.** P3: Sem resultados, o sistema sugere remover filtros. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P4: O usuário abre link externo de referência, quando cadastrado. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Catálogo indisponível: o sistema informa a falha sem inventar informações. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhuma informação do catálogo é alterada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-12, RNF-20. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Explorar e descobrir](../../../prototipo/mockups/explorar.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** O guia apresenta itens ativos e orientações cadastradas, com filtros por categoria.

**Regras relacionadas:** [RN-11](../../requisitos/regras-de-negocio.md#rn-11)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-05 / F-18.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-18.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M03](../../../diagramas-uml/casos-de-uso/M03.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
