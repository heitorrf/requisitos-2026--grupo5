# CDU-10 — Gerenciar Conexões

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Gerenciar Conexões

## 2. Objetivo

Enviar, aceitar, recusar, cancelar ou remover conexões.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

AT-07 — Usuário Acadêmico destinatário (até decidir a solicitação); pode iniciar cenário próprio de decisão.

## 5. Precondições

Os dois perfis existem. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona um perfil elegível e solicita conexão.

**P2.** O sistema verifica bloqueios, conta ativa e inexistência de solicitação ou conexão duplicada.

**P3.** O sistema registra a solicitação pendente para o destinatário.

**P4.** O destinatário consulta a solicitação e aceita.

**P5.** O sistema registra a conexão e apresenta o novo estado aos participantes.

## 7. Fluxos Alternativos

**A1.** P4: O destinatário recusa; o sistema encerra a solicitação sem criar conexão. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: O usuário abre uma conexão existente e a remove; o sistema atualiza o vínculo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P1: O remetente cancela pedido pendente; o sistema encerra a solicitação. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Bloqueio ou solicitação duplicada: o sistema impede novo pedido. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Conexão aceita, recusada, cancelada ou removida conforme o cenário.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Explorar e descobrir](../../../prototipo/mockups/explorar.png) · [Perfil acadêmico](../../../prototipo/mockups/perfil.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Uma conexão somente é criada após aceitação do destinatário; bloqueio impede novo pedido.

**Regras relacionadas:** [RN-03](../../requisitos/regras-de-negocio.md#rn-03), [RN-17](../../requisitos/regras-de-negocio.md#rn-17)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-02 / F-10.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-10.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
