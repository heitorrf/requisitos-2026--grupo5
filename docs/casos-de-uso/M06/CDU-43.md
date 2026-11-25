# CDU-43 — Tratar Denúncias

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Tratar Denúncias

## 2. Objetivo

Analisar evidências autorizadas, registrar decisão e aplicar medidas cabíveis.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-04 — Administrador da Plataforma

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe denúncia registrada. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O administrador abre a fila de denúncias.

**P2.** O sistema apresenta denúncias pendentes com evidências autorizadas e histórico.

**P3.** O administrador analisa a ocorrência, registra decisão fundamentada e seleciona medida cabível.

**P4.** O sistema aplica a medida permitida, registra a decisão e atualiza o estado da denúncia.

## 7. Fluxos Alternativos

**A1.** P3: Sem infração, administrador arquiva com justificativa sem remover conteúdo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Evidência insuficiente: mantém pendente para análise complementar. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A3.** P3: Se a medida exigir suspensão de conta, registra a decisão de acesso conforme RN-12 e CDU-38. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Ação sem autorização ou erro de persistência: o sistema não confirma a medida. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Denúncia tratada ou mantida pendente; medida e justificativa registradas.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-18. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Administração](../../../prototipo/mockups/administracao.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Moderação consegue tratar item denunciado sem abrir todas as mensagens privadas ou notas do denunciado.

**Regras relacionadas:** [RN-04](../../requisitos/regras-de-negocio.md#rn-04), [RN-12](../../requisitos/regras-de-negocio.md#rn-12), [RN-18](../../requisitos/regras-de-negocio.md#rn-18)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-10 / F-43.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-43.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
