# CDU-36 — Definir Idioma da Interface

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M05 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Definir Idioma da Interface

## 2. Objetivo

Selecionar idioma de interface e salvar preferência.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-06 — Visitante, AT-10 — Usuário Autenticado

### 4.2 Secundário

Não se aplica.

## 5. Precondições

Não se aplica. As permissões gerais são verificadas pelo sistema quando a operação exigir acesso restrito.

## 6. Fluxo Principal

**P1.** O usuário abre as preferências de idioma.

**P2.** O sistema apresenta idiomas de interface disponíveis.

**P3.** O usuário seleciona um idioma e confirma.

**P4.** O sistema salva a preferência e atualiza os textos fixos da interface.

## 7. Fluxos Alternativos

**A1.** P3: O usuário mantém a opção anterior ou retorna ao idioma padrão. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P1: Visitante seleciona idioma na tela pública; o sistema mantém preferência local até autenticação, sem exigir conta. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Idioma indisponível: o sistema mantém o anterior e informa a situação. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Preferência registrada na conta ou no navegador quando visitante.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-04, RNF-14, RNF-12. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Média — estimativa a validar.

## 13. Interface Visual

Referência visual: [Acesso e cadastro](../../../prototipo/mockups/acesso.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Alternar português/inglês atualiza textos fixos sem traduzir automaticamente conteúdo de usuários.

**Regras relacionadas:** Nenhuma regra específica; aplicam-se autorização e condições gerais da visão.

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-09 / F-36.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-36.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M05](../../../diagramas-uml/casos-de-uso/M05.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
