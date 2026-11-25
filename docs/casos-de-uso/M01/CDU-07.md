# CDU-07 — Solicitar Perfil Docente

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Solicitar Perfil Docente

## 2. Objetivo

Solicitar autorização docente e consultar estado da solicitação.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante, AT-11 — Candidato a Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

A conta ainda não possui perfil docente autorizado. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O estudante ou candidato abre a solicitação de perfil docente.

**P2.** O sistema apresenta condições e campos de comprovação previstos.

**P3.** O usuário informa instituição, área e referência de comprovação e envia.

**P4.** O sistema registra a solicitação como pendente e apresenta seu estado.

## 7. Fluxos Alternativos

**A1.** P1: Se já houver solicitação, o sistema apresenta seu estado; se recusada, permite nova solicitação corrigida. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: O usuário cancela sem enviar. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Solicitação duplicada ou incompleta: o sistema informa a situação sem conceder permissões. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Solicitação registrada, perfil anterior preservado até decisão administrativa.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Baixa — estimativa a validar.

## 13. Interface Visual

Referência visual: [Perfil acadêmico](../../../prototipo/mockups/perfil.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Uma solicitação pendente não permite criar turmas; decisão de autorização ocorre no CDU-39.

**Regras relacionadas:** [RN-01](../../requisitos/regras-de-negocio.md#rn-01), [RN-02](../../requisitos/regras-de-negocio.md#rn-02), [RN-13](../../requisitos/regras-de-negocio.md#rn-13)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-07.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-07.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
