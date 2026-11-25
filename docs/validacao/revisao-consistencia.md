# Revisão de Consistência UML e SRS — UniShare

<p align="center"><img src="../assets/logo-unishare.png" alt="Logomarca UniShare" width="360"></p>

**Grupo 5 · Versão 1.1 · 25/11/2026**

> Proposta acadêmica para revisão; não representa validação por usuários reais.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |
| 25/11/2026 | 1.1 | Revisão do ZIP atualizado, dos links e da documentação visual | Grupo 5 — proposta |

## Escopo da revisão

Comparação documental entre visão inicial do Grupo 5, versão 3.0, catálogo 4.0, RF, RN, RNF, CDUs, SRS, backlog e UML. Fontes: ZIP mais recente do Grupo 5, pacote documental anterior e guia LAPIS. A revisão é de consistência e estrutura; não equivale à homologação de um sistema real.

## Ajustes efetuados

| Ponto | Problema identificado | Correção |
| --- | --- | --- |
| Visão | Estrutura do SINAIZ com 11 seções não inclui escopo independente do template | Incluída seção 6 e atributos de fonte, valor, frequência e entrega |
| Atores | Professor não autorizado não possuía papel concreto próprio | AT-11 Candidato a Professor; sem funções docentes; herda apenas funções acadêmicas comuns |
| Acesso | Perfil docente podia parecer autoconcedido | Cadastro docente cria candidatura, autorização no CDU-39 |
| Idioma | Preferência não abrangia tela pública ou administração | CDU-36 associado a Visitante e Usuário Autenticado |
| Guia | Orientações de adaptação não estavam explícitas | F-18/F-40 ampliados, preservando IDs |
| UML | Diagramas antigos incompatíveis com catálogo 45 | Seis recortes e hierarquia, além de componentes e implantação atualizados |
| Regras | Prazo, notas, privacidade e bloqueio incompletos | Regras testáveis RN-01 a RN-20, com condições e referências |
| SRS | Ausente na primeira versão do repositório | SRS versionado e 45 especificações individuais |
| Backlog | IDs de requisitos anteriores | RF/CDU atualizados e prioridades propostas |
| Entrevistas | Ausência de evidências reais | Roteiro e análise documental, sem fabricar resultados |

## Revisão da versão atual do repositório

O ZIP recebido continha visão 3.0 e stakeholders anteriores, mas RF/RNF/RN/SRS/matriz da base 4.0; faltavam os arquivos referenciados de CDU, backlog e diagramas novos. A visão foi atualizada a 4.1 sem mudar os 45 IDs. Os RF, RNF, RN e matriz foram preservados do ZIP atual; o SRS 1.1 atualiza a referência visual e o escopo da entrega estática. O README, stakeholders, elicitação, glossário, casos de uso e UML foram conciliados.

## Critérios de verificação documental

- Conferir que cada RF corresponde a uma funcionalidade da visão e a um CDU concreto.
- Conferir associação de atores nos diagramas modulares e validade dos IDs de RN/RNF.
- Conferir que requisitos de gestão acadêmica não concedem acesso a notas de terceiros.
- Conferir que links locais apontam para arquivos do pacote.
- Conferir a cobertura visual e identificar elementos dos mockups não especificados; ver [prototipação](../../prototipo/README.md). As imagens não permitem validar fluxos executáveis.

[Resultados das verificações do pacote](verificacoes.md) · [Matriz](matriz-rastreabilidade.md)

## Resultado da revisão visual

Os mockups foram examinados individualmente. Há elementos ilustrativos fora do escopo (login Google, chamadas, chat coletivo, seguir em vez de conectar, médias oficiais e métricas administrativas). A tabela de ressalvas em [prototipação](../../prototipo/README.md) distingue o comportamento especificado do desenho. Não foram acrescentados requisitos só para reproduzir ícones ou elementos decorativos das imagens. Os novos wireframes refletem a especificação.

## Pendências de validação

Entrevistas reais e revisão por pares; definição de vínculo docente, idioma, catálogo, retenção e moderação; metas de RNF; contrato de serviços externos; confirmação docente sobre dispensa do protótipo navegável; revisão das divergências visuais; conferência de issues/milestones no GitHub. Nenhuma dessas ações é declarada concluída apenas pelo pacote.
