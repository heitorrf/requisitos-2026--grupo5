# CDU-45 — Tratar Solicitação de Exclusão de Conta

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Tratar Solicitação de Exclusão de Conta

## 2. Objetivo

Executar ou encaminhar tratamento de dados conforme política de retenção.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-04 — Administrador da Plataforma

### 4.2 Secundário

AT-07 — solicitante do encerramento de conta.

## 5. Precondições

Existe pedido de exclusão; critérios de retenção aprovados são necessários para conclusão. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O administrador abre pedidos de exclusão.

**P2.** O sistema apresenta pedidos pendentes e dados operacionais necessários, sem expor conteúdo privado desnecessário.

**P3.** O administrador verifica identidade, obrigações de retenção e registra decisão de processamento.

**P4.** O sistema encerra acesso, exclui ou anonimiza dados elegíveis, preserva apenas o necessário conforme política validada e registra conclusão.

## 7. Fluxos Alternativos

**A1.** P3: Política ou obrigação não definida: mantém pedido pendente e registra motivo, sem simular conclusão. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Solicitação inválida: registra decisão de recusa e motivo conforme política aplicável. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Erro de processamento: o sistema registra falha e não marca pedido concluído. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Conta encerrada e tratamento registrado, ou pedido permanece pendente.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18, RNF-22. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Baixa — estimativa a validar.

## 13. Interface Visual

Referência visual: [Administração](../../../prototipo/mockups/administracao.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** O pedido não é marcado concluído sem processamento efetivo; retenção deve ser justificada.

**Regras relacionadas:** [RN-12](../../requisitos/regras-de-negocio.md#rn-12), [RN-14](../../requisitos/regras-de-negocio.md#rn-14)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-45.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-45.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
