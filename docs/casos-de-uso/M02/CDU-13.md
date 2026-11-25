# CDU-13 — Manter Publicação

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Publicação

## 2. Objetivo

Criar, editar e excluir publicações próprias no feed ou grupo autorizado.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Para publicar em grupo restrito, o usuário é participante autorizado. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona criar publicação e escolhe feed ou grupo autorizado.

**P2.** O sistema apresenta formulário de texto, links e anexos permitidos.

**P3.** O usuário preenche o conteúdo e confirma.

**P4.** O sistema verifica autoria, permissões e limites, registra a publicação e a exibe no destino.

## 7. Fluxos Alternativos

**A1.** P1: O autor seleciona publicação própria e edita conteúdo; o sistema valida e salva a alteração. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: O autor seleciona excluir publicação própria, confirma e o sistema retira a publicação da consulta. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P3: Cancelamento mantém o estado anterior. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Formato inválido, ausência de permissão ou falha de gravação: o sistema recusa a operação e informa o motivo. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Publicação criada, atualizada ou retirada pelo autor.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-12, RNF-19. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Feed e publicações](../../../prototipo/mockups/feed.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Usuário publica texto permitido; outro usuário não consegue editar ou excluir a publicação.

**Regras relacionadas:** [RN-04](../../requisitos/regras-de-negocio.md#rn-04), [RN-05](../../requisitos/regras-de-negocio.md#rn-05), [RN-20](../../requisitos/regras-de-negocio.md#rn-20)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-03 / F-13.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-13.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
