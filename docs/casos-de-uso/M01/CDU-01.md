# CDU-01 — Cadastrar Conta

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Cadastrar Conta

## 2. Objetivo

Criar conta estudantil ou candidatura docente e confirmar e-mail.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-06 — Visitante

### 4.2 Secundário

AT-09 — Serviço de E-mail (serviço externo)

## 5. Precondições

Não se aplica. As permissões gerais são verificadas pelo sistema quando a operação exigir acesso restrito.

## 6. Fluxo Principal

**P1.** O visitante informa nome, e-mail, senha e perfil pretendido (local, intercambista ou candidato a professor).

**P2.** O sistema valida campos, unicidade do e-mail e requisitos de senha, registra conta pendente e solicita envio do link de confirmação.

**P3.** O visitante acessa o link recebido.

**P4.** O sistema valida o token, confirma a conta e informa que ela pode ser autenticada.

## 7. Fluxos Alternativos

**A1.** P2: Se já houver conta para o endereço, o sistema orienta a recuperação sem revelar dados da conta. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Se o link estiver vencido, o visitante solicita reenvio; o sistema invalida o anterior e envia novo link. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Se houver falha de envio, o sistema mantém a conta pendente e disponibiliza reenvio; não confirma a conta. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Conta confirmada, sem sessão iniciada; a candidatura não concede permissão docente.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-07, RNF-09, RNF-11, RNF-17. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Baixa — estimativa a validar.

## 13. Interface Visual

Referência visual: [Acesso e cadastro](../../../prototipo/mockups/acesso.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Dado um e-mail ainda não cadastrado, ao concluir a confirmação válida, a conta fica ativa; link expirado não ativa a conta.

**Regras relacionadas:** [RN-01](../../requisitos/regras-de-negocio.md#rn-01), [RN-13](../../requisitos/regras-de-negocio.md#rn-13)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-01.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-01.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
