# CDU-03 — Recuperar Acesso à Conta

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M01 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Recuperar Acesso à Conta

## 2. Objetivo

Restabelecer acesso mediante verificação segura.

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

**P1.** O visitante informa o e-mail para recuperação.

**P2.** O sistema apresenta resposta genérica e, se houver conta elegível, solicita envio de link temporário.

**P3.** O visitante abre o link e informa nova senha.

**P4.** O sistema valida token e senha, altera a credencial, invalida o token e revoga sessões anteriores.

## 7. Fluxos Alternativos

**A1.** P3: Link vencido: o visitante solicita outro link; retorna a P1. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Senha fora dos critérios: o sistema orienta correção e retorna a P3. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Serviço indisponível: o sistema não confirma o envio e permite nova tentativa sem expor dados da conta. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Senha alterada somente com token válido; sessões antigas invalidadas.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-07, RNF-09, RNF-17. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Baixa — estimativa a validar.

## 13. Interface Visual

Referência visual: [Acesso e cadastro](../../../prototipo/mockups/acesso.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Token usado, expirado ou inválido não altera senha; token válido permite acesso com a nova senha.

**Regras relacionadas:** [RN-13](../../requisitos/regras-de-negocio.md#rn-13)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-01 / F-03.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-03.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M01](../../../diagramas-uml/casos-de-uso/M01.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
