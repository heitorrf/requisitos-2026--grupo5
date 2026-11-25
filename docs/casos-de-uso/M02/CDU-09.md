# CDU-09 — Pesquisar Usuários

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Pesquisar Usuários

## 2. Objetivo

Filtrar pessoas por curso, instituição, área, interesses e idiomas.

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

**P1.** O usuário abre a busca de pessoas.

**P2.** O sistema apresenta filtros por curso, instituição, interesses, área e idiomas.

**P3.** O usuário informa um ou mais critérios e realiza a busca.

**P4.** O sistema apresenta perfis correspondentes e acessíveis.

## 7. Fluxos Alternativos

**A1.** P3: Sem critérios, o usuário recebe uma lista inicial paginada. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P4: Sem resultados, o sistema informa a ausência e permite alterar filtros. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Falha na consulta: o sistema informa a falha e mantém os critérios para nova tentativa. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhuma conexão é criada pela busca.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Explorar e descobrir](../../../prototipo/mockups/explorar.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Ao filtrar por área e idioma, aparecem somente perfis elegíveis que atendam aos critérios definidos.

**Regras relacionadas:** [RN-17](../../requisitos/regras-de-negocio.md#rn-17), [RN-19](../../requisitos/regras-de-negocio.md#rn-19)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-02 / F-09.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-09.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
