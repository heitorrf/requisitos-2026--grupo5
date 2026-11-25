# CDU-04 — Encerrar Sessão

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Encerrar Sessão

## 2. Objetivo

Invalidar a sessão corrente.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-10 — Usuário Autenticado

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe sessão corrente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona sair.

**P2.** O sistema invalida a sessão corrente e remove a credencial de sessão do navegador.

**P3.** O sistema apresenta a tela pública de acesso.

## 7. Fluxos Alternativos

**A1.** P1: O usuário cancela a saída, caso a interface apresente confirmação; permanece na tela atual. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Se a sessão já estiver expirada, o sistema limpa a credencial local e apresenta a tela de acesso. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Sessão encerrada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-07, RNF-08, RNF-17. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Acesso e cadastro](../../../prototipo/mockups/acesso.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Após sair, tentar abrir uma página restrita exige autenticação.

**Regras relacionadas:** Nenhuma regra específica; aplicam-se autorização e condições gerais da visão.

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-04.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-04.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
