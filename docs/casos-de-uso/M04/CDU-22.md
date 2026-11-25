# CDU-22 — Manter Turma

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Turma

## 2. Objetivo

Criar, editar e encerrar turmas próprias.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Perfil docente autorizado. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor autorizado seleciona criar turma.

**P2.** O sistema apresenta campos de nome, instituição, disciplina, período e descrição.

**P3.** O professor preenche e confirma.

**P4.** O sistema registra turma sob responsabilidade do professor e apresenta sua área de gestão.

## 7. Fluxos Alternativos

**A1.** P1: Professor seleciona turma própria para editar ou encerrar; o sistema verifica vínculo e confirma a mudança de estado. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Professor cancela sem gravar. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Dados inválidos, falta de autorização ou falha de gravação: o sistema recusa a operação. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Turma criada, editada ou encerrada; encerramento impede novas entregas e ingressos.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-05, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Professor autorizado cria turma; candidato pendente não possui essa permissão.

**Regras relacionadas:** [RN-02](../../requisitos/regras-de-negocio.md#rn-02), [RN-06](../../requisitos/regras-de-negocio.md#rn-06), [RN-15](../../requisitos/regras-de-negocio.md#rn-15)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-22.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-22.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
