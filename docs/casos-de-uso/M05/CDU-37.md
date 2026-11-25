# CDU-37 — Traduzir Conteúdo Textual

<p align="center"><img src="../../assets/logo-unishare.png" alt="Logomarca UniShare" width="250"></p>

**UniShare · M05 · Grupo 5**

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Nome do Caso de Uso

Traduzir Conteúdo Textual

## 2. Objetivo

Solicitar tradução de mensagens, publicações, biografias, descrições e trechos textuais elegíveis.

## 3. Tipo de Caso de Uso

Concreto. Os atores abstratos indicados representam os papéis concretos especializados descritos na visão.

## 4. Atores

### 4.1 Primário

AT-07 — Usuário Acadêmico

### 4.2 Secundário

AT-05 — Serviço de Tradução (serviço externo)

## 5. Precondições

Conteúdo textual acessível ao ator. Autenticação e autorização gerais são condições de acesso verificadas pelo sistema, não inclusões automáticas de outros casos de uso.

## 6. Fluxo Principal

**P1.** O usuário seleciona traduzir em conteúdo textual acessível.

**P2.** O sistema apresenta idioma de destino e verifica autorização e elegibilidade do texto.

**P3.** O usuário confirma o idioma.

**P4.** O sistema envia somente texto necessário ao serviço de tradução, recebe o resultado e exibe versão traduzida identificada, com opção de ver original.

## 7. Fluxos Alternativos

**A1.** P2: Texto já está no idioma escolhido; o sistema mantém o original e informa a situação. O caso termina após a ação descrita, exceto quando houver retorno indicado.

**A2.** P4: Usuário seleciona ver original; o sistema retorna ao texto original. O caso termina após a ação descrita, exceto quando houver retorno indicado.

## 8. Fluxos de Exceção

**E1.** P4: Serviço indisponível, texto não suportado ou falha de tradução: o sistema mantém original e oferece nova tentativa. O caso termina sem confirmar a operação malsucedida, permitindo nova tentativa quando aplicável.

## 9. Pós-condições

Original inalterado; tradução apresentada como resultado auxiliar.

## 10. Requisitos Não Funcionais

Aplicam-se RNF-08, RNF-11, RNF-15, RNF-21. Ver [RNFs](../../requisitos/requisitos-nao-funcionais.md) para condições e métodos de verificação. Não foram identificados RNFs adicionais exclusivos deste caso.

## 12. Frequência de Utilização

Alta — estimativa a validar.

## 13. Interface Visual

Referência visual: [Feed e publicações](../../../prototipo/mockups/feed.png) · [Mensagens](../../../prototipo/mockups/mensagens.png). Consultar [wireframes, cobertura e ressalvas](../../../prototipo/README.md). As imagens ilustram o contexto da funcionalidade; não comprovam execução, permissões ou fluxos alternativos.

## 14. Observações e critério de aceitação

**Aceitação:** Tradução nunca sobrescreve o original; falha do serviço não impede sua leitura.

**Regras relacionadas:** [RN-09](../../requisitos/regras-de-negocio.md#rn-09)

## 15. Referências

- [Visão 4.1](../../01-visao-demanda.md): NEC-09 / F-37.
- [Requisitos funcionais](../../requisitos/requisitos-funcionais.md): RF-37.
- [Glossário](../../requisitos/glossario.md).
- [Diagrama M05](../../../diagramas-uml/casos-de-uso/M05.svg).

## 16. Checklist de validação

- [x] Nome no infinitivo, objetivo e atores identificados.
- [x] Fluxo principal, alternativas, exceções, pós-condições e aceitação registrados.
- [x] Rastreabilidade documental para visão, RF, RN e RNF.
- [ ] Revisão por pares, teste com usuário e aprovação formal.
