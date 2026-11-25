# CDU-17 — Participar de Grupo de Estudo

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M02 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Participar de Grupo de Estudo

## 2. Objetivo

Ingressar, sair e acessar conteúdos do grupo conforme permissões.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

AT-07 — responsável pelo grupo restrito (decisão no CDU-15).

## 5. Precondições

Grupo existente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona grupo disponível.

**P2.** O sistema apresenta regras, descrição e modalidade de ingresso.

**P3.** O usuário solicita participar.

**P4.** O sistema registra participação em grupo aberto ou pedido pendente em grupo restrito, e apresenta o estado.

## 7. Fluxos Alternativos

**A1.** P1: Participante abre grupo e consulta conteúdo autorizado. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: Participante escolhe sair e confirma; o sistema encerra seu vínculo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P4: Em grupo restrito, o responsável decide o pedido pelo CDU-15; até então o conteúdo privado permanece inacessível. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Grupo encerrado ou usuário impedido: o sistema recusa o ingresso. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Participação ativa, pedido pendente ou vínculo encerrado.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Grupos de estudo](../../../prototipo/mockups/grupos.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Pedido pendente de grupo restrito não concede acesso ao conteúdo privado.

**Regras relacionadas:** [RN-05](../../requisitos/regras-de-negocio.md#rn-05)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-04 / F-17.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-17.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M02](../../../diagramas-uml/casos-de-uso/M02.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
