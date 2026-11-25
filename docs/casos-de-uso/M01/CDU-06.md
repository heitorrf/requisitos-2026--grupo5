# CDU-06 — Consultar Perfil Acadêmico

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Perfil Acadêmico

## 2. Objetivo

Visualizar dados de outro usuário conforme visibilidade.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe referência ao perfil consultado. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona o perfil de outra pessoa a partir da busca, de uma conexão ou de uma publicação.

**P2.** O sistema verifica a visibilidade, o estado da conta e restrições de bloqueio.

**P3.** O sistema apresenta os campos autorizados e ações disponíveis de interação.

## 7. Fluxos Alternativos

**A1.** P2: Campo privado é omitido; o sistema mostra apenas os demais campos autorizados. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Perfil indisponível ou bloqueado: o sistema não apresenta os dados restritos. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhum dado do perfil é alterado.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-10, RNF-11. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Perfil acadêmico](../../../prototipo/mockups/perfil.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** A consulta não expõe e-mail privado nem informações acadêmicas restritas.

**Regras relacionadas:** [RN-17](../../requisitos/regras-de-negocio.md#rn-17), [RN-19](../../requisitos/regras-de-negocio.md#rn-19)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-06.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-06.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
