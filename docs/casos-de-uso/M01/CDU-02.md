# CDU-02 — Autenticar Usuário

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Autenticar Usuário

## 2. Objetivo

Iniciar sessão com credenciais válidas.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-06 — Visitante

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Existe conta cadastrada para o cenário de sucesso. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O visitante informa e-mail e senha.

**P2.** O sistema valida as credenciais, a confirmação da conta e seu estado.

**P3.** O sistema cria a sessão e apresenta a página inicial correspondente às permissões.

## 7. Fluxos Alternativos

**A1.** P1: O visitante escolhe recuperar acesso; inicia CDU-03 e encerra este caso de uso. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P2: Conta pendente: o sistema oferece reenvio da confirmação, sem abrir sessão. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Credenciais inválidas ou conta suspensa: o sistema recusa acesso, sem revelar informações sensíveis. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Sessão válida com permissões do perfil efetivo.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-07, RNF-08, RNF-09, RNF-17. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Acesso e cadastro](../../../prototipo/mockups/acesso.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Credenciais válidas de conta ativa abrem sessão; conta não confirmada ou suspensa não entra.

**Regras relacionadas:** [RN-13](../../requisitos/regras-de-negocio.md#rn-13)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-02.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-02.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
