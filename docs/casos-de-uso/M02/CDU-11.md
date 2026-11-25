# CDU-11 — Trocar Mensagens

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Trocar Mensagens

## 2. Objetivo

Enviar mensagens entre conexões aceitas e consultar histórico autorizado.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

AT-07 — Usuário Acadêmico destinatário da mensagem.

## 5. Precondições

Há conexão aceita e participantes autorizados para enviar novas mensagens. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona uma conversa ou um perfil com conexão aceita.

**P2.** O sistema verifica a participação e a inexistência de bloqueio e apresenta o histórico autorizado.

**P3.** O usuário escreve a mensagem e envia.

**P4.** O sistema valida o texto, registra a mensagem e confirma a entrega ao armazenamento, disponibilizando-a ao destinatário.

## 7. Fluxos Alternativos

**A1.** P2: O usuário consulta a conversa sem enviar nova mensagem. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: O usuário cancela a composição; nenhuma mensagem nova é registrada. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Falha de envio: o sistema não apresenta sucesso e permite reenviar; se houver bloqueio, recusa o envio. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Mensagem registrada uma única vez, quando confirmada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-02, RNF-06, RNF-08, RNF-11. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Mensagens](../../../prototipo/mockups/mensagens.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Somente participantes acessam a conversa; envio bloqueado não é armazenado.

**Regras relacionadas:** [RN-03](../../requisitos/regras-de-negocio.md#rn-03), [RN-17](../../requisitos/regras-de-negocio.md#rn-17)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-03 / F-11.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-11.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
