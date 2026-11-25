# CDU-42 — Denunciar Conteúdo

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Denunciar Conteúdo

## 2. Objetivo

Registrar denúncia de conteúdo ou comportamento acessível ao denunciante.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe conteúdo ou comportamento identificável acessível ao ator. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona denunciar conteúdo ou comportamento que pode acessar.

**P2.** O sistema apresenta categorias e campo para descrição da ocorrência.

**P3.** O usuário informa motivo e confirma.

**P4.** O sistema registra denúncia, referência da evidência necessária e estado pendente, sem divulgar a identidade do denunciante ao denunciado.

## 7. Fluxos Alternativos

**A1.** P3: O usuário cancela sem gerar denúncia. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P4: Denúncia já registrada pelo mesmo usuário sobre o mesmo item: o sistema informa estado existente. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Conteúdo inacessível ou descrição inválida: o sistema recusa registro indevido. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Denúncia pendente registrada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Feed e publicações](../../../prototipo/mockups/feed.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Denúncia válida gera item para moderação e não concede acesso a informações privadas adicionais.

**Regras relacionadas:** [RN-18](../../requisitos/regras-de-negocio.md#rn-18)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-42.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-42.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
