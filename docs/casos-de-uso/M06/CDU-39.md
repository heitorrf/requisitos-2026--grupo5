# CDU-39 — Analisar Solicitação de Perfil Docente

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Analisar Solicitação de Perfil Docente

## 2. Objetivo

Autorizar ou recusar solicitação com base em critérios de verificação.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-04 — Administrador da Plataforma

### 4.2 Secundário

AT-08 ou AT-11 — solicitante, recebe decisão.

## 5. Precondições

Existe solicitação pendente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O administrador abre solicitações docentes.

**P2.** O sistema apresenta pedidos pendentes e informações de comprovação autorizadas.

**P3.** O administrador seleciona pedido, verifica os critérios e registra decisão de autorizar.

**P4.** O sistema registra a decisão, atribui perfil docente efetivo e apresenta estado ao solicitante.

## 7. Fluxos Alternativos

**A1.** P3: Administrador recusa com justificativa; o sistema mantém perfil anterior e apresenta estado ao solicitante. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Comprovação insuficiente: administrador mantém pendente e solicita complemento pelo registro do pedido. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Pedido já decidido ou operação sem autorização: o sistema não modifica o perfil. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Decisão auditável; autorização somente se critérios atendidos.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Baixa — estimativa a validar.

## 13. Interface Visual

Referência visual: [Administração](../../../prototipo/mockups/administracao.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Somente administrador autorizado concede perfil docente; candidato não ganha permissão enquanto pendente.

**Regras relacionadas:** [RN-01](../../requisitos/regras-de-negocio.md#rn-01), [RN-02](../../requisitos/regras-de-negocio.md#rn-02), [RN-12](../../requisitos/regras-de-negocio.md#rn-12)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-39.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-39.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
