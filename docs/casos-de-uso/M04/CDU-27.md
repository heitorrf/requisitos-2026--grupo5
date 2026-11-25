# CDU-27 — Consultar Materiais Acadêmicos

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Materiais Acadêmicos

## 2. Objetivo

Acessar materiais das turmas autorizadas.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante, AT-03 — Professor

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe turma com vínculo autorizado ou responsabilidade docente. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O estudante ou professor abre materiais de uma turma acessível.

**P2.** O sistema valida o vínculo e apresenta a lista de materiais.

**P3.** O usuário seleciona um item.

**P4.** O sistema apresenta descrição e disponibiliza o arquivo ou link autorizado.

## 7. Fluxos Alternativos

**A1.** P2: Lista vazia: o sistema informa ausência de materiais. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: O usuário consulta apenas a descrição sem abrir o arquivo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Arquivo removido, acesso revogado ou falha de carregamento: o sistema informa sem expor o arquivo. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhum material é alterado.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-19. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Turmas](../../../prototipo/mockups/turmas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** A consulta e download respeitam as mesmas permissões da turma.

**Regras relacionadas:** [RN-06](../../requisitos/regras-de-negocio.md#rn-06), [RN-20](../../requisitos/regras-de-negocio.md#rn-20)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-07 / F-27.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-27.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
