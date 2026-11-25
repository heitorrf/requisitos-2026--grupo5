# CDU-12 — Consultar Publicações

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Publicações

## 2. Objetivo

Visualizar feed e publicações acessíveis.

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

**P1.** O usuário abre o feed.

**P2.** O sistema verifica a visibilidade das publicações e apresenta uma lista em ordem de atualização definida.

**P3.** O usuário seleciona uma publicação ou carrega mais resultados.

**P4.** O sistema apresenta o conteúdo e as interações acessíveis.

## 7. Fluxos Alternativos

**A1.** P3: O usuário filtra por área ou acessa publicações de um grupo do qual participa. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Se não houver conteúdo elegível, o sistema mostra estado vazio. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Falha na consulta: o sistema informa indisponibilidade e oferece nova tentativa. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhuma publicação alterada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Feed e publicações](../../../prototipo/mockups/feed.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Publicações removidas ou de grupo restrito sem participação não aparecem.

**Regras relacionadas:** [RN-05](../../requisitos/regras-de-negocio.md#rn-05)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-03 / F-12.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-12.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
