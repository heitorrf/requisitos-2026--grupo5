# CDU-26 — Manter Material Acadêmico

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Material Acadêmico

## 2. Objetivo

Publicar, atualizar e retirar materiais de turmas próprias.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Turma existente sob responsabilidade do professor. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor seleciona materiais de uma turma própria.

**P2.** O sistema apresenta campos de título, descrição e arquivo ou link.

**P3.** O professor informa material e confirma.

**P4.** O sistema valida permissão e formato, grava e disponibiliza para participantes autorizados.

## 7. Fluxos Alternativos

**A1.** P1: Professor edita ou retira material próprio; o sistema atualiza sua disponibilidade. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Cancelamento não altera registros. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Arquivo fora dos limites ou erro de armazenamento: o sistema não publica o material. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Material disponível ou alterado conforme a ação.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-05, RNF-19. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Aluno autorizado visualiza material; aluno sem vínculo não obtém o arquivo por link direto.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06), [RN-20](../../requisitos/regras-de-negocio.md#rn-20)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-26.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-26.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
