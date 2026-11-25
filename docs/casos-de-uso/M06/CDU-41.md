# CDU-41 — Manter Catálogos de Apoio

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Catálogos de Apoio

## 2. Objetivo

Manter áreas, interesses, categorias e referências de conteúdo para recomendações.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-04 — Administrador da Plataforma

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Não se aplica. As permissões gerais são verificadas pelo sistema quando a operação exigir acesso restrito.

## 6. Fluxo Principal

**P1.** O administrador abre catálogos de apoio.

**P2.** O sistema apresenta áreas, interesses, categorias e referências de recomendações.

**P3.** O administrador seleciona categoria e cadastra uma referência com título, tema e fonte.

**P4.** O sistema valida unicidade e dados, registra a referência e a torna elegível às recomendações.

## 7. Fluxos Alternativos

**A1.** P1: Administrador edita ou inativa item; o sistema preserva vínculos históricos e retira item das novas sugestões. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Administrador cadastra ou mantém área, interesse ou categoria. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Duplicidade ou referência inválida: o sistema recusa o cadastro. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Catálogo atualizado, sem perda indevida de referências existentes.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-18, RNF-20. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Administração](../../../prototipo/mockups/administracao.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Item inativo deixa de aparecer em novas recomendações; categorias não são duplicadas.

**Regras relacionadas:** [RN-10](../../requisitos/regras-de-negocio.md#rn-10), [RN-11](../../requisitos/regras-de-negocio.md#rn-11)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-06 / F-41.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-41.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
