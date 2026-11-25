# CDU-21 — Consultar Recomendações

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M03 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Recomendações

## 2. Objetivo

Receber sugestões de livros, aulas, cursos, conteúdos e eventos por área e interesses.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Perfil e catálogo disponíveis para personalização. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário abre a seção de recomendações.

**P2.** O sistema consulta área, interesses e catálogo de referências elegíveis.

**P3.** O sistema ordena resultados por afinidade e apresenta livros, aulas, cursos, eventos e conteúdos disponíveis com indicação de tema.

**P4.** O usuário seleciona um item para consultar sua referência.

## 7. Fluxos Alternativos

**A1.** P2: Sem interesses definidos, o sistema apresenta sugestões gerais e orienta completar o perfil. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Sem itens elegíveis, apresenta estado vazio. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Erro de consulta: o sistema não inventa recomendações e informa indisponibilidade. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhum dado externo é cadastrado pela consulta.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-12, RNF-20. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Explorar e descobrir](../../../prototipo/mockups/explorar.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Perfis com áreas distintas recebem sugestões coerentes com as categorias cadastradas.

**Regras relacionadas:** [RN-10](../../requisitos/regras-de-negocio.md#rn-10), [RN-11](../../requisitos/regras-de-negocio.md#rn-11)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-06 / F-21.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-21.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M03](../../../diagramas-uml/casos-de-uso/M03.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
