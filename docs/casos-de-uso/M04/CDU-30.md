# CDU-30 — Submeter Atividade

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Submeter Atividade

## 2. Objetivo

Entregar trabalho e consultar situação de sua entrega.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Atividade publicada, turma ativa e vínculo autorizado. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O estudante abre atividade disponível.

**P2.** O sistema verifica vínculo, prazo e instruções de entrega.

**P3.** O estudante informa resposta ou anexa arquivo permitido e confirma.

**P4.** O sistema valida prazo e conteúdo, grava a entrega e apresenta recibo com data e estado.

## 7. Fluxos Alternativos

**A1.** P1: Estudante consulta entrega própria já registrada. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Antes do prazo, estudante substitui a entrega quando a atividade permitir; o sistema registra nova versão. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Prazo vencido, turma encerrada, arquivo inválido ou falha de gravação: o sistema não confirma nova entrega. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Entrega registrada com data; nenhuma nota atribuída automaticamente.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-05, RNF-08, RNF-19. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Atividades e entregas](../../../prototipo/mockups/atividades.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Entrega válida dentro do prazo recebe confirmação; fora do prazo é recusada pela regra inicial.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06), [RN-07](../../requisitos/regras-de-negocio.md#rn-07), [RN-15](../../requisitos/regras-de-negocio.md#rn-15), [RN-20](../../requisitos/regras-de-negocio.md#rn-20)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-08 / F-30.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-30.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
