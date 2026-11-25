# CDU-40 — Manter Catálogo de Locais

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M06 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Manter Catálogo de Locais

## 2. Objetivo

Cadastrar, atualizar e retirar locais recomendados e orientações do guia.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-04 — Administrador da Plataforma

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Não se aplica. As permissões gerais são verificadas pelo sistema quando a operação exigir acesso restrito.

## 6. Fluxo Principal

**P1.** O administrador abre o catálogo de locais e orientações.

**P2.** O sistema apresenta campos de nome, categoria, descrição, localização ou instrução, fonte e data de atualização.

**P3.** O administrador preenche os dados e confirma.

**P4.** O sistema valida campos, registra item e disponibiliza no guia.

## 7. Fluxos Alternativos

**A1.** P1: Administrador edita ou retira item; o sistema registra alteração e atualiza visibilidade. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P3: Cancelamento preserva catálogo. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Fonte ou dados obrigatórios ausentes, ou falha de gravação: o sistema não publica. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Item cadastrado, atualizado ou retirado.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-18, RNF-20. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Administração](../../../prototipo/mockups/administracao.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Somente itens ativos do catálogo aparecem no guia; referência e data permitem avaliar atualidade.

**Regras relacionadas:** [RN-11](../../requisitos/regras-de-negocio.md#rn-11)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-05 / F-40.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-40.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M06](../../../diagramas-uml/casos-de-uso/M06.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
