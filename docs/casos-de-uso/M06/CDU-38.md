# CDU-38 — Gerenciar Usuários e Acessos

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Gerenciar Usuários e Acessos

## 2. Objetivo

Consultar contas e suspender ou restabelecer acesso conforme autorização.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-04 — Administrador da Plataforma

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe conta elegível para ação administrativa. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O administrador abre gestão de contas.

**P2.** O sistema apresenta dados operacionais mínimos, estado e perfil de contas.

**P3.** O administrador seleciona conta e informa motivo da suspensão.

**P4.** O sistema verifica sua autorização, registra a suspensão, revoga sessões da conta e grava a ação em histórico.

## 7. Fluxos Alternativos

**A1.** P3: Administrador restabelece conta elegível com justificativa; o sistema restaura acesso sem conceder privilégios novos. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Administrador filtra contas sem alterar estado. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Operação não autorizada, conta administrativa protegida ou falha de registro: o sistema recusa a alteração. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Estado da conta atualizado com registro de ação.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Administração](../../../prototipo/mockups/administracao.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Conta suspensa não autentica; gestão não disponibiliza mensagens ou notas privadas.

**Regras relacionadas:** [RN-01](../../requisitos/regras-de-negocio.md#rn-01), [RN-12](../../requisitos/regras-de-negocio.md#rn-12)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-38.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-38.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
