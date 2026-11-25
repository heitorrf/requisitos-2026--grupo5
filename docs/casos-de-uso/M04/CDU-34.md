# CDU-34 — Manter Comunicado

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Comunicado

## 2. Objetivo

Publicar, editar e retirar avisos de turmas próprias.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Turma sob responsabilidade do professor. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O professor abre comunicados de turma própria.

**P2.** O sistema apresenta formulário de título e texto.

**P3.** O professor preenche e confirma.

**P4.** O sistema registra o comunicado e o apresenta aos participantes autorizados.

## 7. Fluxos Alternativos

**A1.** P1: Professor edita ou retira comunicado próprio; o sistema atualiza a exibição. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Cancelamento preserva registros. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Conteúdo inválido, acesso indevido ou falha de gravação: o sistema não publica. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Comunicado criado, editado ou retirado.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-05, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Participantes da turma veem o aviso; usuários externos à turma não o consultam.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-34.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-34.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
