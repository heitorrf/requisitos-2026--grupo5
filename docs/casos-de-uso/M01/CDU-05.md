# CDU-05 — Manter Perfil Acadêmico

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Perfil Acadêmico

## 2. Objetivo

Consultar e alterar dados próprios, biografia, instituição, curso ou área, interesses e idiomas.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe perfil associado à conta. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário abre seu perfil.

**P2.** O sistema apresenta dados editáveis e a visibilidade de cada campo.

**P3.** O usuário altera biografia, instituição, curso ou área, interesses ou idiomas e salva.

**P4.** O sistema valida os dados, registra as mudanças e apresenta o perfil atualizado.

## 7. Fluxos Alternativos

**A1.** P3: O usuário apenas consulta ou cancela alterações; o sistema conserva os dados anteriores. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: O usuário altera a visibilidade de campos opcionais; o sistema aplica a escolha nas consultas posteriores. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Campo inválido ou falha de gravação: o sistema não confirma a atualização e mantém os dados anteriores. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Alterações válidas persistidas, sem mudança de permissões privilegiadas.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Perfil acadêmico](../../../prototipo/mockups/perfil.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Alterar a biografia modifica o perfil próprio, mas não permite conceder perfil docente ou administrativo.

**Regras relacionadas:** [RN-01](../../requisitos/regras-de-negocio.md#rn-01), [RN-10](../../requisitos/regras-de-negocio.md#rn-10), [RN-19](../../requisitos/regras-de-negocio.md#rn-19)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-05.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-05.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
