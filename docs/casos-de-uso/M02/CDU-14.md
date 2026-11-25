# CDU-14 — Interagir com Publicações

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Interagir com Publicações

## 2. Objetivo

Comentar, reagir e salvar publicações acessíveis; manter interações próprias.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Publicação acessível. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona uma publicação acessível.

**P2.** O sistema apresenta reações, comentários e ação de salvar.

**P3.** O usuário escreve um comentário e confirma.

**P4.** O sistema registra o comentário com autoria e atualiza a exibição.

## 7. Fluxos Alternativos

**A1.** P3: O usuário reage ou desfaz a reação; o sistema atualiza a reação única por usuário. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: O usuário salva ou remove dos salvos; o sistema atualiza apenas sua coleção. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P3: O autor edita ou exclui seu próprio comentário; o sistema aplica a alteração. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Publicação indisponível, comentário inválido ou acesso revogado: o sistema recusa a interação. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Interação registrada, alterada ou removida conforme ação.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Feed e publicações](../../../prototipo/mockups/feed.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Reação pode ser desfeita; salvar não altera a visibilidade para outros usuários.

**Regras relacionadas:** [RN-04](../../requisitos/regras-de-negocio.md#rn-04)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-03 / F-14.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-14.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
