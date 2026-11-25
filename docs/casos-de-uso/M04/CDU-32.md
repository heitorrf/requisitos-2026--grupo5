# CDU-32 — Consultar Desempenho Individual

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M04 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Consultar Desempenho Individual

## 2. Objetivo

Acessar notas e feedback próprios.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-08 — Estudante

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Há vínculo acadêmico autorizado. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O estudante abre seu desempenho acadêmico.

**P2.** O sistema identifica os vínculos e consulta apenas notas e feedback do próprio estudante.

**P3.** O estudante seleciona turma ou atividade.

**P4.** O sistema apresenta resultados disponíveis, pontuação máxima e estado de avaliação.

## 7. Fluxos Alternativos

**A1.** P2: Se não houver nota, apresenta aguardando avaliação, sem interpretar como zero. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Estudante consulta outra turma da qual participa. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P2: Tentativa de acessar resultado de outro estudante: o sistema recusa a consulta. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Nenhum resultado é alterado.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-01, RNF-08, RNF-10. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Notas e desempenho](../../../prototipo/mockups/notas.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Usuário não pode obter notas de outro estudante pela interface nem por requisição direta.

**Regras relacionadas:** [RN-07](../../requisitos/regras-de-negocio.md#rn-07), [RN-08](../../requisitos/regras-de-negocio.md#rn-08), [RN-16](../../requisitos/regras-de-negocio.md#rn-16)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-08 / F-32.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-32.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M04](../../../diagramas-uml/casos-de-uso/M04.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
