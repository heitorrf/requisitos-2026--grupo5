# Backlog Inicial Priorizado

**Projeto:** Rede Social Acadêmica Internacional  
**Grupo:** 5  
**Artefato:** Backlog inicial do produto

## 1. Objetivo

Este documento apresenta as funcionalidades previstas para a Rede Social Acadêmica Internacional, organizadas por prioridade. A proposta busca aproximar estudantes intercambistas, estudantes locais e professores, facilitando a comunicação, a adaptação ao campus e a colaboração acadêmica por meio de uma plataforma multilíngue.

O backlog representa o **planejamento inicial do produto**. A ordem apresentada orienta uma possível evolução da plataforma e não indica que as funcionalidades já foram implementadas.

## 2. Critério de priorização

A priorização utiliza o método **MoSCoW**, considerando a importância de cada funcionalidade para a proposta principal:

- **Must Have — Essencial:** necessário para a primeira versão voltada à integração e à comunicação entre estudantes.
- **Should Have — Importante:** amplia a experiência acadêmica e a utilidade da plataforma, podendo ser desenvolvido após a base essencial.
- **Could Have — Complementar:** agrega valor, mas pode ser incorporado em uma etapa posterior.

Dentro de cada categoria, a numeração indica uma **ordem sugerida de planejamento**, sujeita às dependências entre funcionalidades.

## 3. Backlog priorizado

| ID | Funcionalidade | Prioridade | Descrição | Requisitos relacionados |
|---|---|---|---|---|
| **PB01** | Acesso à plataforma | Must Have | Permitir que estudantes e professores acessem suas contas por autenticação. | RF01 |
| **PB02** | Perfil acadêmico | Must Have | Permitir a criação e a atualização de perfis com instituição, curso ou área de atuação e interesses. | RF02 |
| **PB03** | Busca e integração entre estudantes | Must Have | Localizar estudantes por curso, área e interesses, incluindo a identificação de estudantes locais para contato com intercambistas. | RF03 |
| **PB04** | Conexões acadêmicas | Must Have | Permitir solicitações de conexão entre estudantes, com aceitação ou recusa pelo destinatário. | RF04 |
| **PB05** | Mensagens | Must Have | Permitir a troca de mensagens entre usuários da plataforma. | RF05 |
| **PB06** | Idioma da interface | Must Have | Permitir a escolha de um idioma disponível para os elementos da interface. | RF16 |
| **PB07** | Tradução de conteúdos | Must Have | Permitir a tradução sob demanda de textos, como mensagens, publicações, biografias, descrições e guias. | RF17 |
| **PB08** | Publicações e materiais | Should Have | Permitir a criação, a consulta e o compartilhamento de conteúdos acadêmicos. | RF07 |
| **PB09** | Grupos de estudo | Should Have | Permitir a consulta e a participação em grupos e comunidades acadêmicas. | RF06 |
| **PB10** | Guia de adaptação ao campus | Should Have | Disponibilizar orientações para a adaptação de estudantes intercambistas. | RF08 |
| **PB11** | Consulta acadêmica | Should Have | Permitir que estudantes consultem suas atividades, seus prazos e suas notas. | RF11 |
| **PB12** | Gestão de atividades | Should Have | Permitir que professores criem e atualizem atividades e prazos de suas turmas. | RF12 |
| **PB13** | Materiais e comunicados docentes | Should Have | Permitir que professores publiquem conteúdos e avisos acadêmicos para suas turmas. | RF13 |
| **PB14** | Notas e desempenho acadêmico | Should Have | Permitir que professores registrem e atualizem notas e consultem o desempenho de estudantes de suas turmas. | RF14, RF15 |
| **PB15** | Eventos e locais recomendados | Could Have | Permitir a consulta de eventos, pontos turísticos, locais de estudo e espaços de convivência. | RF09 |
| **PB16** | Filtros por área de conhecimento | Could Have | Permitir a filtragem de conteúdos e eventos por área de conhecimento ou interesse acadêmico. | RF10 |

## 4. Critérios de aceitação

Os critérios abaixo descrevem resultados observáveis para cada item do backlog.

| ID | Critério de aceitação |
|---|---|
| **PB01** | Um estudante ou professor com conta cadastrada consegue autenticar-se e acessar sua conta. |
| **PB02** | O usuário consegue cadastrar e atualizar as informações de seu próprio perfil acadêmico. |
| **PB03** | A busca retorna perfis compatíveis com os filtros escolhidos e permite identificar estudantes locais. |
| **PB04** | Um estudante consegue enviar uma solicitação de conexão; o destinatário consegue aceitá-la ou recusá-la. |
| **PB05** | Um usuário consegue enviar uma mensagem e o destinatário consegue visualizá-la. |
| **PB06** | Ao selecionar um idioma disponível, o usuário visualiza os textos fixos da interface nesse idioma. |
| **PB07** | O usuário consegue solicitar uma tradução e visualizar o resultado sem alteração do texto original. |
| **PB08** | O usuário consegue publicar e consultar conteúdos acadêmicos compartilhados. |
| **PB09** | O usuário consegue consultar grupos e participar daqueles aos quais possui acesso. |
| **PB10** | O intercambista consegue consultar orientações de adaptação ao campus. |
| **PB11** | O estudante consegue visualizar atividades, prazos e notas associados à sua conta. |
| **PB12** | Um professor autorizado consegue cadastrar e atualizar uma atividade e seu prazo na turma correspondente. |
| **PB13** | Um professor autorizado consegue publicar materiais e comunicados para sua turma. |
| **PB14** | Um professor autorizado consegue registrar ou atualizar notas e consultar o desempenho de estudantes de sua turma. |
| **PB15** | O usuário consegue consultar informações cadastradas sobre eventos e locais recomendados. |
| **PB16** | Ao selecionar uma área de conhecimento ou interesse, o usuário visualiza conteúdos ou eventos correspondentes ao filtro. |

## 5. Dependências principais

| Item | Dependência |
|---|---|
| **PB02** | PB01, para associar o perfil a uma conta. |
| **PB03** | PB02, para disponibilizar as informações acadêmicas utilizadas na busca. |
| **PB04** | PB01 e PB03, para identificar usuários e localizar possíveis conexões. |
| **PB05** | PB01, para identificar remetente e destinatário. |
| **PB07** | Conteúdos textuais disponíveis na plataforma; o idioma de destino deve ser suportado. A tradução pode ser utilizada com o idioma da interface definido em PB06. |
| **PB09** | PB01, para identificar os participantes. |
| **PB11–PB14** | PB01 e identificação dos vínculos acadêmicos necessários ao controle de acesso. |
| **PB16** | PB08 ou PB15, conforme o tipo de conteúdo ou evento a ser filtrado. |

## 6. Relação com os demais artefatos

Este backlog foi organizado com base no **Documento de Visão** e na **Especificação de Requisitos Funcionais e Não Funcionais**. A coluna de requisitos da seção 3 estabelece a correspondência entre cada item `PB` e os requisitos `RF`.

As **Regras de Negócio** complementam os itens do backlog, especialmente quanto à autoria de publicações, à aceitação de conexões, às permissões acadêmicas e à preservação dos textos originais nas traduções. Os **diagramas UML** representam as principais interações e a arquitetura proposta para essas funcionalidades.

## 7. Organização no GitHub

Os itens deste documento podem ser registrados como *issues* do backlog do produto, mantendo seus identificadores nos títulos, por exemplo: `PB07 — Tradução de conteúdos`.

O **backlog do produto** descreve funcionalidades planejadas para a plataforma. Já as **issues da Sprint 1** devem acompanhar as atividades de documentação e modelagem exigidas na disciplina. Esses dois acompanhamentos têm finalidades diferentes.

---

**Grupo 5 — Rede Social Acadêmica Internacional**
