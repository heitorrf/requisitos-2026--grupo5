# Especificação de Regras de Negócio

**Projeto:** Rede Social Acadêmica Internacional  
**Grupo:** 5  
**Artefato:** Regras de Negócio (RNG)  
**Versão:** 1.0 — proposta para avaliação

## 1. Apresentação

Este documento reúne as regras de negócio previstas para a Rede Social Acadêmica Internacional, plataforma proposta para aproximar estudantes locais, intercambistas e professores. As regras estabelecem condições e restrições para o uso de perfis, conexões, comunidades, recursos acadêmicos e funcionalidades de internacionalização.

A especificação foi elaborada com base no Documento de Visão e nos diagramas UML do Grupo 5, seguindo as orientações de documentação de regras de negócio do modelo LAPIS. As regras constituem a **proposta atual do grupo** e estão sujeitas à validação com os envolvidos. Não são apresentadas como resultados de entrevistas já realizadas.

## 2. Regras de negócio

### 2.1. Perfis e conexões

#### RN01 — Usuários editam seus próprios perfis

- **Regra:** Um usuário pode alterar somente as informações do perfil acadêmico associado à sua conta.
- **Condição de aplicação:** O usuário solicita a edição de um perfil.
- **Resultado esperado:** A alteração é permitida se o perfil pertence ao usuário autenticado; caso contrário, é recusada.
- **Referência:** Caso de uso *Gerenciar perfil acadêmico*.
- **Origem:** Restrição proposta a partir do gerenciamento de perfis previsto no Documento de Visão.

#### RN02 — Estudantes aceitam solicitações de conexão

- **Regra:** Uma conexão acadêmica entre estudantes somente é estabelecida após a aceitação da solicitação pelo destinatário.
- **Condição de aplicação:** Um estudante envia uma solicitação de conexão a outro estudante.
- **Resultado esperado:** A conexão permanece pendente até a aceitação; uma solicitação recusada não gera conexão.
- **Referência:** Caso de uso *Criar conexões acadêmicas*.
- **Origem:** Decisão de funcionamento proposta pelo grupo; o mecanismo de aceitação não está definido no Documento de Visão.

### 2.2. Comunidades e publicações

#### RN03 — Membros publicam em grupos restritos

- **Regra:** Somente membros de um grupo classificado como restrito podem publicar conteúdo em suas discussões internas.
- **Condição de aplicação:** Um usuário tenta publicar em um grupo restrito.
- **Resultado esperado:** A publicação é permitida para membros e recusada para não membros.
- **Referência:** Caso de uso *Participar de grupos de estudo*.
- **Origem:** Proposta de controle de participação; a existência de grupos restritos ainda deve ser confirmada.

#### RN04 — Autores editam suas próprias publicações

- **Regra:** A edição de uma publicação é permitida somente ao usuário que a criou.
- **Condição de aplicação:** Um usuário solicita a edição de uma publicação.
- **Resultado esperado:** A edição é permitida quando o solicitante é o autor; caso contrário, é recusada.
- **Referência:** Caso de uso *Compartilhar publicações e materiais*.
- **Origem:** Proposta de controle de autoria; eventuais permissões de moderação não estão definidas nesta versão.

### 2.3. Gestão acadêmica

#### RN05 — Professores responsáveis gerenciam atividades de suas turmas

- **Regra:** Um professor pode criar ou alterar atividades acadêmicas apenas das turmas ou disciplinas sob sua responsabilidade.
- **Condição de aplicação:** Um professor solicita a criação ou alteração de uma atividade vinculada a uma turma ou disciplina.
- **Resultado esperado:** A operação é permitida quando existe vínculo de responsabilidade com a turma ou disciplina; caso contrário, é recusada.
- **Referência:** Caso de uso *Gerenciar atividades e prazos*.
- **Origem:** Restrição proposta a partir das atribuições dos professores descritas no Documento de Visão.

#### RN06 — Professores autorizados registram notas

- **Regra:** Somente professores autorizados para uma turma ou disciplina podem registrar ou alterar notas de seus estudantes.
- **Condição de aplicação:** Um usuário solicita o registro ou a alteração de uma nota.
- **Resultado esperado:** A operação é permitida quando o usuário possui autorização docente para a turma ou disciplina correspondente; caso contrário, é recusada.
- **Referência:** Caso de uso *Registrar notas e acompanhar desempenho*.
- **Origem:** Restrição proposta a partir do controle de notas previsto no Documento de Visão.

#### RN07 — Estudantes consultam suas próprias notas

- **Regra:** Um estudante pode consultar somente as notas e os resultados acadêmicos associados à sua conta.
- **Condição de aplicação:** Um estudante solicita a consulta de notas ou resultados acadêmicos.
- **Resultado esperado:** A consulta apresenta os dados do próprio estudante e não disponibiliza dados de outros estudantes.
- **Referência:** Caso de uso *Consultar atividades, prazos e notas*.
- **Origem:** Restrição de acesso proposta a partir da funcionalidade de acompanhamento acadêmico.

#### RN08 — Professores autorizados publicam comunicados em suas turmas

- **Regra:** Um professor pode publicar comunicados vinculados a uma turma ou disciplina somente quando possui autorização para ela.
- **Condição de aplicação:** Um professor solicita a publicação de um comunicado acadêmico.
- **Resultado esperado:** A publicação é permitida quando a autorização para a turma ou disciplina está presente; caso contrário, é recusada.
- **Referência:** Caso de uso *Publicar materiais e comunicados*.
- **Origem:** Restrição proposta a partir da comunicação acadêmica prevista no Documento de Visão.

### 2.4. Idioma e tradução

#### RN09 — Traduções preservam o texto original

- **Regra:** A tradução de um conteúdo textual não pode substituir nem modificar o texto original armazenado na plataforma.
- **Condição de aplicação:** Um usuário solicita a tradução de uma mensagem, publicação, descrição ou outro texto compatível.
- **Resultado esperado:** A tradução é exibida separadamente, mantendo o conteúdo original inalterado.
- **Referência:** Caso de uso *Traduzir conteúdo textual sob demanda*.
- **Origem:** Restrição proposta para o recurso de tradução incluído na visão atualizada do projeto.

#### RN10 — Usuários selecionam idiomas disponíveis para tradução

- **Regra:** O idioma de destino de uma tradução deve pertencer ao conjunto de idiomas disponibilizados pela plataforma.
- **Condição de aplicação:** Um usuário escolhe o idioma de destino ao solicitar uma tradução.
- **Resultado esperado:** A seleção aceita somente idiomas disponíveis; idiomas não oferecidos não podem ser escolhidos.
- **Referência:** Caso de uso *Traduzir conteúdo textual sob demanda*.
- **Origem:** Regra operacional proposta para delimitar as opções de tradução; a lista de idiomas ainda não foi definida.

### 2.5. Recomendações e integração

#### RN11 — Filtros acadêmicos restringem conteúdos à área selecionada

- **Regra:** Ao aplicar um filtro de área de conhecimento, o sistema deve apresentar somente conteúdos classificados na área selecionada.
- **Condição de aplicação:** Um estudante filtra conteúdos acadêmicos por área de conhecimento.
- **Resultado esperado:** Os conteúdos retornados possuem classificação correspondente à área escolhida.
- **Referência:** Funcionalidade de recomendação e filtragem por área de conhecimento prevista no Documento de Visão; **não há caso de uso específico para essa filtragem nos diagramas atuais**.
- **Origem:** Regra proposta a partir da filtragem por área descrita na Proposta de Valor.

#### RN12 — Filtros de localidade restringem eventos e locais recomendados

- **Regra:** Ao aplicar um filtro de localidade, o sistema deve apresentar somente eventos e locais associados à localidade selecionada.
- **Condição de aplicação:** Um estudante filtra eventos ou locais recomendados por localidade.
- **Resultado esperado:** Os resultados correspondem à localidade escolhida.
- **Referência:** Caso de uso *Consultar eventos e locais recomendados*.
- **Origem:** Regra proposta para detalhar a consulta de eventos e locais; a existência desse filtro ainda deve ser confirmada.

## 3. Pontos para validação

As regras anteriores representam a especificação proposta pelo Grupo 5. Antes de considerá-las aprovadas pelos stakeholders, é necessário confirmar:

- **Conexões e comunidades:** necessidade de aceitação das conexões, existência de grupos restritos e permissões de participação.
- **Publicações:** permissões de edição e eventual atuação de moderadores.
- **Gestão acadêmica:** forma de vincular professores a turmas ou disciplinas e critérios de autorização para notas, atividades e comunicados.
- **Internacionalização:** idiomas disponíveis e comportamento esperado da tradução.
- **Recomendações e integração:** classificação dos conteúdos por área e disponibilidade de filtros de localidade.

Esses pontos não impedem a apresentação do documento como **proposta de especificação**, mas devem ser revisados à medida que o grupo realizar a elicitação e a validação dos requisitos.

## 4. Referências e rastreabilidade

Este artefato foi construído a partir dos seguintes materiais do projeto:

- **Documento de Visão:** objetivos, públicos beneficiados e funcionalidades propostas.
- **Diagrama de Casos de Uso:** funcionalidades e interações previstas para estudantes e professores.
- **Diagramas de Componentes e Implantação:** organização lógica e infraestrutura proposta para a plataforma.
- **Modelo LAPIS:** orientações para identificação, descrição e verificação de regras de negócio.

Os identificadores `RN01` a `RN12` podem ser utilizados em outros artefatos do grupo, incluindo requisitos, casos de uso, backlog e issues do GitHub.
