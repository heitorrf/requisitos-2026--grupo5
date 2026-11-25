# CDU-20 — Divulgar Evento ou Oportunidade

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M03 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Divulgar Evento ou Oportunidade

## 2. Objetivo

Cadastrar, atualizar e retirar divulgações próprias.

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

**P1.** O professor autorizado abre a área de divulgações.

**P2.** O sistema apresenta campos de título, tipo, área, descrição, datas, modalidade e referência.

**P3.** O professor preenche e confirma.

**P4.** O sistema valida datas e autoria, registra a divulgação e a disponibiliza no catálogo.

## 7. Fluxos Alternativos

**A1.** P1: Professor seleciona divulgação própria para editar ou retirar; o sistema verifica autoria e aplica a alteração. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: O professor cancela o cadastro. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Datas incoerentes, falta de autorização ou falha de gravação: o sistema recusa e mantém o estado anterior. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Divulgação criada, atualizada ou retirada.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-12, RNF-20. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Explorar e descobrir](../../../prototipo/mockups/explorar.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Professor divulga evento com período válido; outro professor não pode editar a divulgação sem autorização.

**Regras relacionadas:** [RN-11](../../requisitos/regras-de-negocio.md#rn-11)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-05 / F-20.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-20.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M03](../../../diagramas-uml/casos-de-uso/M03.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
