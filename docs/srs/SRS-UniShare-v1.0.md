# Especificação de Requisitos de Software (SRS) — UniShare

**Grupo 5 · Versão 1.0 · 25/11/2026**

> Proposta acadêmica para revisão; não representa validação por usuários reais.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Introdução

### 1.1 Propósito

Especificar os requisitos do UniShare para orientar desenvolvimento, modelagem, testes e avaliação acadêmica. Documento organizado segundo a estrutura de SRS solicitada na P2 (IEEE 830: introdução, descrição geral e requisitos específicos), complementada pelos modelos LAPIS de casos de uso, regras de negócio e RNFs.

### 1.2 Escopo

Rede social acadêmica web que facilita integração cultural e colaboração entre estudantes locais, intercambistas e professores. Inclui perfis, comunicação, grupos, guia de adaptação, eventos, recomendações, turmas internas, tradução sob demanda e administração. Não substitui sistemas acadêmicos oficiais, nem inclui pagamento, chamada de vídeo, aplicativo nativo ou tradução multimídia.

### 1.3 Definições, acrônimos e abreviações

Consultar [glossário](../requisitos/glossario.md). Identificadores NEC, F, RF, CDU, RN e RNF têm correspondência rastreável.

### 1.4 Referências

- [Visão da Demanda 4.0](../01-visao-demanda.md).
- [LAPIS — guia e templates](https://github.com/marcelobezerra-dotcom/Lapis-unifor).
- Orientações de P1 e P2 apresentadas pelo professor; a referência IEEE 830 é a estrutura solicitada na atividade, não certificação de conformidade normativa.

### 1.5 Organização

A seção 2 descreve produto, públicos, restrições e premissas. A seção 3 especifica interfaces, RFs, CDUs, regras e qualidade. Os arquivos individuais de CDU complementam esta SRS e fazem parte da mesma versão documental.

## 2. Descrição Geral

### 2.1 Perspectiva do produto

O UniShare é independente de sistemas institucionais e opera pela web. Navegador interage com aplicação, que controla autorização, persistência e integrações externas de tradução textual e e-mail. A implantação e arquitetura são propostas, não implementações existentes.

### 2.2 Funções do produto

| Módulo | Funções | CDUs |
| --- | --- | --- |
| M01 — Identidade e Perfis | Cadastrar Conta; Autenticar Usuário; Recuperar Acesso à Conta; Encerrar Sessão; Manter Perfil Acadêmico; Consultar Perfil Acadêmico; Solicitar Perfil Docente; Solicitar Exclusão de Conta | CDU-01 a CDU-08 |
| M02 — Rede Social e Comunicação | Pesquisar Usuários; Gerenciar Conexões; Trocar Mensagens; Consultar Publicações; Manter Publicação; Interagir com Publicações; Manter Grupo de Estudo; Pesquisar Grupos de Estudo; Participar de Grupo de Estudo | CDU-09 a CDU-17 |
| M03 — Integração Cultural e Descoberta | Consultar Locais Recomendados; Consultar Eventos e Oportunidades; Divulgar Evento ou Oportunidade; Consultar Recomendações | CDU-18 a CDU-21 |
| M04 — Gestão Acadêmica | Manter Turma; Consultar Turmas; Solicitar Participação em Turma; Gerenciar Participantes da Turma; Manter Material Acadêmico; Consultar Materiais Acadêmicos; Manter Atividade; Consultar Atividades; Submeter Atividade; Avaliar Entregas; Consultar Desempenho Individual; Acompanhar Desempenho da Turma; Manter Comunicado; Consultar Comunicados | CDU-22 a CDU-35 |
| M05 — Acessibilidade Linguística | Definir Idioma da Interface; Traduzir Conteúdo Textual | CDU-36 a CDU-37 |
| M06 — Administração e Moderação | Gerenciar Usuários e Acessos; Analisar Solicitação de Perfil Docente; Manter Catálogo de Locais; Manter Catálogos de Apoio; Denunciar Conteúdo; Tratar Denúncias; Bloquear Usuário; Tratar Solicitação de Exclusão de Conta | CDU-38 a CDU-45 |

### 2.3 Características dos usuários

| Ator | Papel |
| --- | --- |
| AT-01 | Estudante Local |
| AT-02 | Estudante Intercambista |
| AT-03 | Professor |
| AT-04 | Administrador da Plataforma |
| AT-05 | Serviço de Tradução |
| AT-06 | Visitante |
| AT-07 | Usuário Acadêmico |
| AT-08 | Estudante |
| AT-09 | Serviço de E-mail |
| AT-10 | Usuário Autenticado |
| AT-11 | Candidato a Professor |

Visitante utiliza funções públicas; usuários acadêmicos usam funções sociais; estudantes usam operações de turma e resultados próprios; professores autorizados gerenciam turmas próprias. Candidato docente não herda operações de professor. Administrador atua em governança sem acesso irrestrito a notas ou mensagens. A hierarquia UML abstrai funções comuns; serviços externos são secundários.

### 2.4 Restrições

Aplicação web, autenticação e autorização no servidor, textos em idiomas suportados, dados acadêmicos internos, fontes externas sujeitas a viabilidade. Proposta acadêmica sem autorização para processamento real de dados. Ver [RNFs](../requisitos/requisitos-nao-funcionais.md).

### 2.5 Premissas e dependências

Português e inglês inicialmente; serviço de tradução textual e serviço de e-mail a selecionar. O conteúdo de descoberta requer manutenção administrativa. Critérios de comprovação docente, retenção, moderação e limites devem ser validados. Nenhuma entrevista real foi fornecida; a especificação permanece proposta.

### 2.6 Requisitos distribuídos por entrega

E1 concentra identidade, rede social, descoberta, idioma e governança. E2 concentra gestão acadêmica. Os dois recortes integram a especificação P2 e não representam implementação concluída. A ordem depende de revisão de valor, risco e capacidade da equipe.

## 3. Requisitos Específicos

### 3.1 Interfaces externas

| Interface | Interação | Condições |
| --- | --- | --- |
| Usuário / navegador | Formulários, feed, busca, conversas, turmas, configurações e administração | Interface responsiva, navegação por teclado e feedback de operações |
| Serviço de tradução (AT-05) | Texto elegível e idioma de destino; resposta traduzida ou falha | Envio mínimo de dados; original preservado; contrato a definir |
| Serviço de e-mail (AT-09) | Solicitação de confirmação/recuperação e resposta de entrega/erro | Tokens temporários; sem senha em mensagens ou logs; fornecedor a definir |
| Persistência interna | Contas, perfis, conexões, publicações, grupos, catálogos, turmas, entregas, notas e auditoria | Não é ator externo; autorização, integridade e retenção |

### 3.2 Requisitos funcionais e casos de uso

O requisito abaixo identifica a capacidade, seu objetivo, atores, regras relacionadas, resultado e critério verificável. Os links apontam para a especificação completa de fluxos principal, alternativos e de exceção no padrão LAPIS. O texto das seções e os arquivos CDU integram esta SRS versionada.

#### M01 — Identidade e Perfis

##### RF-01 — Cadastrar Conta

O sistema deverá disponibilizar aos atores indicados a opção de criar conta estudantil ou candidatura docente e confirmar e-mail.

**Atores:** AT-06, AT-09 · **Origem:** NEC-01 / F-01 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O visitante informa nome, e-mail, senha e perfil pretendido (local, intercambista ou candidato a professor). O sistema valida campos, unicidade do e-mail e requisitos de senha, registra conta pendente e solicita envio do link de confirmação. O visitante acessa o link recebido. O sistema valida o token, confirma a conta e informa que ela pode ser autenticada.

**Resultado:** Conta confirmada, sem sessão iniciada; a candidatura não concede permissão docente.

**Critério de aceitação:** Dado um e-mail ainda não cadastrado, ao concluir a confirmação válida, a conta fica ativa; link expirado não ativa a conta.

**Restrições:** RN-01, RN-13; RNF-07, RNF-09, RNF-11, RNF-17. **Fluxos detalhados:** [CDU-01](../casos-de-uso/M01/CDU-01.md).

##### RF-02 — Autenticar Usuário

O sistema deverá disponibilizar aos atores indicados a opção de iniciar sessão com credenciais válidas.

**Atores:** AT-06 · **Origem:** NEC-01 / F-02 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O visitante informa e-mail e senha. O sistema valida as credenciais, a confirmação da conta e seu estado. O sistema cria a sessão e apresenta a página inicial correspondente às permissões.

**Resultado:** Sessão válida com permissões do perfil efetivo.

**Critério de aceitação:** Credenciais válidas de conta ativa abrem sessão; conta não confirmada ou suspensa não entra.

**Restrições:** RN-13; RNF-07, RNF-08, RNF-09, RNF-17. **Fluxos detalhados:** [CDU-02](../casos-de-uso/M01/CDU-02.md).

##### RF-03 — Recuperar Acesso à Conta

O sistema deverá disponibilizar aos atores indicados a opção de restabelecer acesso mediante verificação segura.

**Atores:** AT-06, AT-09 · **Origem:** NEC-01 / F-03 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O visitante informa o e-mail para recuperação. O sistema apresenta resposta genérica e, se houver conta elegível, solicita envio de link temporário. O visitante abre o link e informa nova senha. O sistema valida token e senha, altera a credencial, invalida o token e revoga sessões anteriores.

**Resultado:** Senha alterada somente com token válido; sessões antigas invalidadas.

**Critério de aceitação:** Token usado, expirado ou inválido não altera senha; token válido permite acesso com a nova senha.

**Restrições:** RN-13; RNF-07, RNF-09, RNF-17. **Fluxos detalhados:** [CDU-03](../casos-de-uso/M01/CDU-03.md).

##### RF-04 — Encerrar Sessão

O sistema deverá oferecer aos atores autorizados a capacidade de invalidar a sessão corrente.

**Atores:** AT-10 · **Origem:** NEC-01 / F-04 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona sair. O sistema invalida a sessão corrente e remove a credencial de sessão do navegador. O sistema apresenta a tela pública de acesso.

**Resultado:** Sessão encerrada.

**Critério de aceitação:** Após sair, tentar abrir uma página restrita exige autenticação.

**Restrições:** Condições gerais da visão; RNF-07, RNF-08, RNF-17. **Fluxos detalhados:** [CDU-04](../casos-de-uso/M01/CDU-04.md).

##### RF-05 — Manter Perfil Acadêmico

O sistema deverá oferecer aos atores autorizados a capacidade de consultar e alterar dados próprios, biografia, instituição, curso ou área, interesses e idiomas.

**Atores:** AT-07 · **Origem:** NEC-01 / F-05 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre seu perfil. O sistema apresenta dados editáveis e a visibilidade de cada campo. O usuário altera biografia, instituição, curso ou área, interesses ou idiomas e salva. O sistema valida os dados, registra as mudanças e apresenta o perfil atualizado.

**Resultado:** Alterações válidas persistidas, sem mudança de permissões privilegiadas.

**Critério de aceitação:** Alterar a biografia modifica o perfil próprio, mas não permite conceder perfil docente ou administrativo.

**Restrições:** RN-01, RN-10, RN-19; RNF-08, RNF-11, RNF-12. **Fluxos detalhados:** [CDU-05](../casos-de-uso/M01/CDU-05.md).

##### RF-06 — Consultar Perfil Acadêmico

O sistema deverá oferecer aos atores autorizados a capacidade de visualizar dados de outro usuário conforme visibilidade.

**Atores:** AT-07 · **Origem:** NEC-01 / F-06 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona o perfil de outra pessoa a partir da busca, de uma conexão ou de uma publicação. O sistema verifica a visibilidade, o estado da conta e restrições de bloqueio. O sistema apresenta os campos autorizados e ações disponíveis de interação.

**Resultado:** Nenhum dado do perfil é alterado.

**Critério de aceitação:** A consulta não expõe e-mail privado nem informações acadêmicas restritas.

**Restrições:** RN-17, RN-19; RNF-08, RNF-10, RNF-11. **Fluxos detalhados:** [CDU-06](../casos-de-uso/M01/CDU-06.md).

##### RF-07 — Solicitar Perfil Docente

O sistema deverá oferecer aos atores autorizados a capacidade de solicitar autorização docente e consultar estado da solicitação.

**Atores:** AT-08, AT-11 · **Origem:** NEC-10 / F-07 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O estudante ou candidato abre a solicitação de perfil docente. O sistema apresenta condições e campos de comprovação previstos. O usuário informa instituição, área e referência de comprovação e envia. O sistema registra a solicitação como pendente e apresenta seu estado.

**Resultado:** Solicitação registrada, perfil anterior preservado até decisão administrativa.

**Critério de aceitação:** Uma solicitação pendente não permite criar turmas; decisão de autorização ocorre no CDU-39.

**Restrições:** RN-01, RN-02, RN-13; RNF-08, RNF-11, RNF-18. **Fluxos detalhados:** [CDU-07](../casos-de-uso/M01/CDU-07.md).

##### RF-08 — Solicitar Exclusão de Conta

O sistema deverá oferecer aos atores autorizados a capacidade de solicitar encerramento da conta e tratamento dos dados conforme política aplicável.

**Atores:** AT-07 · **Origem:** NEC-01 / F-08 · **Prioridade:** Importante · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona excluir conta. O sistema explica consequências e dados sujeitos a retenção e solicita confirmação. O usuário confirma a identidade e a solicitação. O sistema registra pedido pendente e informa o acompanhamento.

**Resultado:** Pedido de exclusão registrado, sem apagar dados imediatamente.

**Critério de aceitação:** Cancelar não altera a conta; confirmar gera pedido rastreável para CDU-45.

**Restrições:** RN-14; RNF-08, RNF-11, RNF-18. **Fluxos detalhados:** [CDU-08](../casos-de-uso/M01/CDU-08.md).

#### M02 — Rede Social e Comunicação

##### RF-09 — Pesquisar Usuários

O sistema deverá oferecer aos atores autorizados a capacidade de filtrar pessoas por curso, instituição, área, interesses e idiomas.

**Atores:** AT-07 · **Origem:** NEC-02 / F-09 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre a busca de pessoas. O sistema apresenta filtros por curso, instituição, interesses, área e idiomas. O usuário informa um ou mais critérios e realiza a busca. O sistema apresenta perfis correspondentes e acessíveis.

**Resultado:** Nenhuma conexão é criada pela busca.

**Critério de aceitação:** Ao filtrar por área e idioma, aparecem somente perfis elegíveis que atendam aos critérios definidos.

**Restrições:** RN-17, RN-19; RNF-01, RNF-08, RNF-12. **Fluxos detalhados:** [CDU-09](../casos-de-uso/M02/CDU-09.md).

##### RF-10 — Gerenciar Conexões

O sistema deverá oferecer aos atores autorizados a capacidade de enviar, aceitar, recusar, cancelar ou remover conexões.

**Atores:** AT-07 · **Origem:** NEC-02 / F-10 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona um perfil elegível e solicita conexão. O sistema verifica bloqueios, conta ativa e inexistência de solicitação ou conexão duplicada. O sistema registra a solicitação pendente para o destinatário. O destinatário consulta a solicitação e aceita. O sistema registra a conexão e apresenta o novo estado aos participantes.

**Resultado:** Conexão aceita, recusada, cancelada ou removida conforme o cenário.

**Critério de aceitação:** Uma conexão somente é criada após aceitação do destinatário; bloqueio impede novo pedido.

**Restrições:** RN-03, RN-17; RNF-08, RNF-11. **Fluxos detalhados:** [CDU-10](../casos-de-uso/M02/CDU-10.md).

##### RF-11 — Trocar Mensagens

O sistema deverá oferecer aos atores autorizados a capacidade de enviar mensagens entre conexões aceitas e consultar histórico autorizado.

**Atores:** AT-07 · **Origem:** NEC-03 / F-11 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona uma conversa ou um perfil com conexão aceita. O sistema verifica a participação e a inexistência de bloqueio e apresenta o histórico autorizado. O usuário escreve a mensagem e envia. O sistema valida o texto, registra a mensagem e confirma a entrega ao armazenamento, disponibilizando-a ao destinatário.

**Resultado:** Mensagem registrada uma única vez, quando confirmada.

**Critério de aceitação:** Somente participantes acessam a conversa; envio bloqueado não é armazenado.

**Restrições:** RN-03, RN-17; RNF-02, RNF-06, RNF-08, RNF-11. **Fluxos detalhados:** [CDU-11](../casos-de-uso/M02/CDU-11.md).

##### RF-12 — Consultar Publicações

O sistema deverá oferecer aos atores autorizados a capacidade de visualizar feed e publicações acessíveis.

**Atores:** AT-07 · **Origem:** NEC-03 / F-12 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre o feed. O sistema verifica a visibilidade das publicações e apresenta uma lista em ordem de atualização definida. O usuário seleciona uma publicação ou carrega mais resultados. O sistema apresenta o conteúdo e as interações acessíveis.

**Resultado:** Nenhuma publicação alterada.

**Critério de aceitação:** Publicações removidas ou de grupo restrito sem participação não aparecem.

**Restrições:** RN-05; RNF-01, RNF-08, RNF-12. **Fluxos detalhados:** [CDU-12](../casos-de-uso/M02/CDU-12.md).

##### RF-13 — Manter Publicação

O sistema deverá oferecer aos atores autorizados a capacidade de criar, editar e excluir publicações próprias no feed ou grupo autorizado.

**Atores:** AT-07 · **Origem:** NEC-03 / F-13 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona criar publicação e escolhe feed ou grupo autorizado. O sistema apresenta formulário de texto, links e anexos permitidos. O usuário preenche o conteúdo e confirma. O sistema verifica autoria, permissões e limites, registra a publicação e a exibe no destino.

**Resultado:** Publicação criada, atualizada ou retirada pelo autor.

**Critério de aceitação:** Usuário publica texto permitido; outro usuário não consegue editar ou excluir a publicação.

**Restrições:** RN-04, RN-05, RN-20; RNF-08, RNF-12, RNF-19. **Fluxos detalhados:** [CDU-13](../casos-de-uso/M02/CDU-13.md).

##### RF-14 — Interagir com Publicações

O sistema deverá oferecer aos atores autorizados a capacidade de comentar, reagir e salvar publicações acessíveis; manter interações próprias.

**Atores:** AT-07 · **Origem:** NEC-03 / F-14 · **Prioridade:** Importante · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona uma publicação acessível. O sistema apresenta reações, comentários e ação de salvar. O usuário escreve um comentário e confirma. O sistema registra o comentário com autoria e atualiza a exibição.

**Resultado:** Interação registrada, alterada ou removida conforme ação.

**Critério de aceitação:** Reação pode ser desfeita; salvar não altera a visibilidade para outros usuários.

**Restrições:** RN-04; RNF-08, RNF-12. **Fluxos detalhados:** [CDU-14](../casos-de-uso/M02/CDU-14.md).

##### RF-15 — Manter Grupo de Estudo

O sistema deverá oferecer aos atores autorizados a capacidade de criar e manter grupos de estudo e gerenciar participantes quando responsável.

**Atores:** AT-07 · **Origem:** NEC-04 / F-15 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona criar grupo de estudo. O sistema apresenta campos de nome, tema, descrição e modalidade de ingresso. O usuário informa os dados e confirma. O sistema cria o grupo, registra o criador como responsável e apresenta o grupo.

**Resultado:** Grupo criado ou mantido, com participação controlada.

**Critério de aceitação:** Criador pode administrar seu grupo; participante comum não consegue aprovar pedidos de ingresso.

**Restrições:** RN-05; RNF-08, RNF-12. **Fluxos detalhados:** [CDU-15](../casos-de-uso/M02/CDU-15.md).

##### RF-16 — Pesquisar Grupos de Estudo

O sistema deverá oferecer aos atores autorizados a capacidade de localizar grupos por tema ou área.

**Atores:** AT-07 · **Origem:** NEC-04 / F-16 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre a busca de grupos. O sistema apresenta filtros de tema, área e modalidade. O usuário informa critérios e pesquisa. O sistema apresenta grupos disponíveis com descrição e situação de participação.

**Resultado:** Nenhuma participação é alterada.

**Critério de aceitação:** Busca retorna grupos que correspondem aos filtros, sem revelar publicações restritas.

**Restrições:** RN-05; RNF-01, RNF-08, RNF-12. **Fluxos detalhados:** [CDU-16](../casos-de-uso/M02/CDU-16.md).

##### RF-17 — Participar de Grupo de Estudo

O sistema deverá oferecer aos atores autorizados a capacidade de ingressar, sair e acessar conteúdos do grupo conforme permissões.

**Atores:** AT-07 · **Origem:** NEC-04 / F-17 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona grupo disponível. O sistema apresenta regras, descrição e modalidade de ingresso. O usuário solicita participar. O sistema registra participação em grupo aberto ou pedido pendente em grupo restrito, e apresenta o estado.

**Resultado:** Participação ativa, pedido pendente ou vínculo encerrado.

**Critério de aceitação:** Pedido pendente de grupo restrito não concede acesso ao conteúdo privado.

**Restrições:** RN-05; RNF-08, RNF-12. **Fluxos detalhados:** [CDU-17](../casos-de-uso/M02/CDU-17.md).

#### M03 — Integração Cultural e Descoberta

##### RF-18 — Consultar Locais Recomendados

O sistema deverá oferecer aos atores autorizados a capacidade de consultar guia de adaptação, orientações, locais de estudo, convivência, serviços e pontos turísticos.

**Atores:** AT-07 · **Origem:** NEC-05 / F-18 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre o guia de adaptação. O sistema apresenta categorias de locais, serviços do campus, convivência, pontos turísticos e orientações. O usuário filtra por categoria ou instituição e seleciona um item. O sistema apresenta descrição, referência de localização e data de atualização quando disponíveis.

**Resultado:** Nenhuma informação do catálogo é alterada.

**Critério de aceitação:** O guia apresenta itens ativos e orientações cadastradas, com filtros por categoria.

**Restrições:** RN-11; RNF-01, RNF-12, RNF-20. **Fluxos detalhados:** [CDU-18](../casos-de-uso/M03/CDU-18.md).

##### RF-19 — Consultar Eventos e Oportunidades

O sistema deverá oferecer aos atores autorizados a capacidade de pesquisar palestras, workshops, congressos, vagas e oportunidades.

**Atores:** AT-07 · **Origem:** NEC-05 / F-19 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre eventos e oportunidades. O sistema apresenta filtros de área, data, categoria e modalidade. O usuário seleciona critérios e pesquisa. O sistema apresenta divulgações acessíveis com título, descrição, prazo e referência quando informados.

**Resultado:** Nenhuma divulgação alterada.

**Critério de aceitação:** Filtro de oportunidades abertas não inclui prazos encerrados; detalhes indicam a fonte fornecida.

**Restrições:** RN-11; RNF-01, RNF-12, RNF-20. **Fluxos detalhados:** [CDU-19](../casos-de-uso/M03/CDU-19.md).

##### RF-20 — Divulgar Evento ou Oportunidade

O sistema deverá oferecer aos atores autorizados a capacidade de cadastrar, atualizar e retirar divulgações próprias.

**Atores:** AT-03 · **Origem:** NEC-05 / F-20 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O professor autorizado abre a área de divulgações. O sistema apresenta campos de título, tipo, área, descrição, datas, modalidade e referência. O professor preenche e confirma. O sistema valida datas e autoria, registra a divulgação e a disponibiliza no catálogo.

**Resultado:** Divulgação criada, atualizada ou retirada.

**Critério de aceitação:** Professor divulga evento com período válido; outro professor não pode editar a divulgação sem autorização.

**Restrições:** RN-11; RNF-08, RNF-12, RNF-20. **Fluxos detalhados:** [CDU-20](../casos-de-uso/M03/CDU-20.md).

##### RF-21 — Consultar Recomendações

O sistema deverá oferecer aos atores autorizados a capacidade de receber sugestões de livros, aulas, cursos, conteúdos e eventos por área e interesses.

**Atores:** AT-07 · **Origem:** NEC-06 / F-21 · **Prioridade:** Importante · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre a seção de recomendações. O sistema consulta área, interesses e catálogo de referências elegíveis. O sistema ordena resultados por afinidade e apresenta livros, aulas, cursos, eventos e conteúdos disponíveis com indicação de tema. O usuário seleciona um item para consultar sua referência.

**Resultado:** Nenhum dado externo é cadastrado pela consulta.

**Critério de aceitação:** Perfis com áreas distintas recebem sugestões coerentes com as categorias cadastradas.

**Restrições:** RN-10, RN-11; RNF-01, RNF-12, RNF-20. **Fluxos detalhados:** [CDU-21](../casos-de-uso/M03/CDU-21.md).

#### M04 — Gestão Acadêmica

##### RF-22 — Manter Turma

O sistema deverá oferecer aos atores autorizados a capacidade de criar, editar e encerrar turmas próprias.

**Atores:** AT-03 · **Origem:** NEC-07 / F-22 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor autorizado seleciona criar turma. O sistema apresenta campos de nome, instituição, disciplina, período e descrição. O professor preenche e confirma. O sistema registra turma sob responsabilidade do professor e apresenta sua área de gestão.

**Resultado:** Turma criada, editada ou encerrada; encerramento impede novas entregas e ingressos.

**Critério de aceitação:** Professor autorizado cria turma; candidato pendente não possui essa permissão.

**Restrições:** RN-02, RN-06, RN-15; RNF-08, RNF-05, RNF-12. **Fluxos detalhados:** [CDU-22](../casos-de-uso/M04/CDU-22.md).

##### RF-23 — Consultar Turmas

O sistema deverá oferecer aos atores autorizados a capacidade de visualizar turmas acessíveis e respectivos dados.

**Atores:** AT-08, AT-03 · **Origem:** NEC-07 / F-23 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O usuário abre turmas. O sistema apresenta turmas próprias para professor ou turmas disponíveis e vínculos para estudante. O usuário seleciona uma turma. O sistema apresenta somente informações públicas ou informações da turma autorizadas para seu vínculo.

**Resultado:** Nenhum vínculo criado pela consulta.

**Critério de aceitação:** Estudante não inscrito não visualiza materiais privados; professor vê suas turmas.

**Restrições:** RN-06; RNF-01, RNF-08, RNF-10. **Fluxos detalhados:** [CDU-23](../casos-de-uso/M04/CDU-23.md).

##### RF-24 — Solicitar Participação em Turma

O sistema deverá oferecer aos atores autorizados a capacidade de solicitar ingresso em turma ou cancelar pedido pendente.

**Atores:** AT-08 · **Origem:** NEC-07 / F-24 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O estudante seleciona uma turma aberta a ingressos ou informa convite. O sistema apresenta dados da turma e verifica elegibilidade. O estudante confirma a solicitação. O sistema registra pedido pendente e informa que aguarda decisão do professor.

**Resultado:** Pedido pendente sem acesso privado até aprovação.

**Critério de aceitação:** Solicitar ingresso não libera materiais; autorização depende do CDU-25.

**Restrições:** RN-06; RNF-08, RNF-12. **Fluxos detalhados:** [CDU-24](../casos-de-uso/M04/CDU-24.md).

##### RF-25 — Gerenciar Participantes da Turma

O sistema deverá oferecer aos atores autorizados a capacidade de autorizar ou recusar ingresso e gerenciar participantes de turmas próprias.

**Atores:** AT-03 · **Origem:** NEC-07 / F-25 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor abre os participantes de uma turma própria. O sistema apresenta vínculos ativos e pedidos pendentes. O professor seleciona pedido e autoriza a participação. O sistema registra decisão, ativa o vínculo e atualiza as permissões de acesso à turma.

**Resultado:** Vínculo ativo, recusado ou revogado, com histórico.

**Critério de aceitação:** Somente responsável autorizado decide ingresso; estudante aprovado pode consultar materiais.

**Restrições:** RN-06; RNF-08, RNF-10, RNF-18. **Fluxos detalhados:** [CDU-25](../casos-de-uso/M04/CDU-25.md).

##### RF-26 — Manter Material Acadêmico

O sistema deverá oferecer aos atores autorizados a capacidade de publicar, atualizar e retirar materiais de turmas próprias.

**Atores:** AT-03 · **Origem:** NEC-07 / F-26 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor seleciona materiais de uma turma própria. O sistema apresenta campos de título, descrição e arquivo ou link. O professor informa material e confirma. O sistema valida permissão e formato, grava e disponibiliza para participantes autorizados.

**Resultado:** Material disponível ou alterado conforme a ação.

**Critério de aceitação:** Aluno autorizado visualiza material; aluno sem vínculo não obtém o arquivo por link direto.

**Restrições:** RN-06, RN-20; RNF-08, RNF-05, RNF-19. **Fluxos detalhados:** [CDU-26](../casos-de-uso/M04/CDU-26.md).

##### RF-27 — Consultar Materiais Acadêmicos

O sistema deverá oferecer aos atores autorizados a capacidade de acessar materiais das turmas autorizadas.

**Atores:** AT-08, AT-03 · **Origem:** NEC-07 / F-27 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O estudante ou professor abre materiais de uma turma acessível. O sistema valida o vínculo e apresenta a lista de materiais. O usuário seleciona um item. O sistema apresenta descrição e disponibiliza o arquivo ou link autorizado.

**Resultado:** Nenhum material é alterado.

**Critério de aceitação:** A consulta e download respeitam as mesmas permissões da turma.

**Restrições:** RN-06, RN-20; RNF-01, RNF-08, RNF-19. **Fluxos detalhados:** [CDU-27](../casos-de-uso/M04/CDU-27.md).

##### RF-28 — Manter Atividade

O sistema deverá oferecer aos atores autorizados a capacidade de criar, atualizar e encerrar tarefas, exercícios e avaliações com prazo.

**Atores:** AT-03 · **Origem:** NEC-07 / F-28 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor abre atividades de turma própria. O sistema apresenta campos de título, instruções, prazo, pontuação máxima e forma de entrega. O professor preenche e confirma. O sistema valida prazo, pontuação e autorização, grava e publica a atividade.

**Resultado:** Atividade publicada, atualizada ou encerrada.

**Critério de aceitação:** Atividade com prazo e pontuação válidos é visível aos participantes; encerrada não aceita novas entregas.

**Restrições:** RN-06, RN-15, RN-16; RNF-05, RNF-08, RNF-18. **Fluxos detalhados:** [CDU-28](../casos-de-uso/M04/CDU-28.md).

##### RF-29 — Consultar Atividades

O sistema deverá oferecer aos atores autorizados a capacidade de acessar orientações, prazos e situação das atividades.

**Atores:** AT-08, AT-03 · **Origem:** NEC-07 / F-29 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O usuário abre atividades de turma acessível. O sistema valida vínculo e apresenta atividades com prazo e estado. O usuário seleciona atividade. O sistema apresenta instruções e estado da entrega própria, ou visão de gestão para professor responsável.

**Resultado:** Nenhuma atividade ou entrega alterada.

**Critério de aceitação:** Estudante visualiza apenas o estado de sua própria entrega; professor acessa as informações de gestão da turma.

**Restrições:** RN-06, RN-07, RN-15; RNF-01, RNF-08, RNF-10. **Fluxos detalhados:** [CDU-29](../casos-de-uso/M04/CDU-29.md).

##### RF-30 — Submeter Atividade

O sistema deverá oferecer aos atores autorizados a capacidade de entregar trabalho e consultar situação de sua entrega.

**Atores:** AT-08 · **Origem:** NEC-08 / F-30 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O estudante abre atividade disponível. O sistema verifica vínculo, prazo e instruções de entrega. O estudante informa resposta ou anexa arquivo permitido e confirma. O sistema valida prazo e conteúdo, grava a entrega e apresenta recibo com data e estado.

**Resultado:** Entrega registrada com data; nenhuma nota atribuída automaticamente.

**Critério de aceitação:** Entrega válida dentro do prazo recebe confirmação; fora do prazo é recusada pela regra inicial.

**Restrições:** RN-06, RN-07, RN-15, RN-20; RNF-05, RNF-08, RNF-19. **Fluxos detalhados:** [CDU-30](../casos-de-uso/M04/CDU-30.md).

##### RF-31 — Avaliar Entregas

O sistema deverá oferecer aos atores autorizados a capacidade de avaliar entregas, atribuir notas dentro da escala da atividade e atualizar feedback.

**Atores:** AT-03 · **Origem:** NEC-08 / F-31 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor abre entregas de atividade de turma própria. O sistema verifica responsabilidade e lista entregas autorizadas. O professor seleciona entrega, informa nota e feedback e confirma. O sistema valida faixa de pontuação, grava a avaliação e disponibiliza somente ao estudante avaliado.

**Resultado:** Avaliação registrada ou atualizada; estudante pode consultar a própria.

**Critério de aceitação:** Nota superior à pontuação máxima é rejeitada; avaliação válida aparece apenas para o aluno avaliado e professor responsável.

**Restrições:** RN-07, RN-08, RN-16; RNF-05, RNF-08, RNF-10, RNF-18. **Fluxos detalhados:** [CDU-31](../casos-de-uso/M04/CDU-31.md).

##### RF-32 — Consultar Desempenho Individual

O sistema deverá oferecer aos atores autorizados a capacidade de acessar notas e feedback próprios.

**Atores:** AT-08 · **Origem:** NEC-08 / F-32 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O estudante abre seu desempenho acadêmico. O sistema identifica os vínculos e consulta apenas notas e feedback do próprio estudante. O estudante seleciona turma ou atividade. O sistema apresenta resultados disponíveis, pontuação máxima e estado de avaliação.

**Resultado:** Nenhum resultado é alterado.

**Critério de aceitação:** Usuário não pode obter notas de outro estudante pela interface nem por requisição direta.

**Restrições:** RN-07, RN-08, RN-16; RNF-01, RNF-08, RNF-10. **Fluxos detalhados:** [CDU-32](../casos-de-uso/M04/CDU-32.md).

##### RF-33 — Acompanhar Desempenho da Turma

O sistema deverá oferecer aos atores autorizados a capacidade de consultar resultados individuais e coletivos de turmas próprias.

**Atores:** AT-03 · **Origem:** NEC-08 / F-33 · **Prioridade:** Importante · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor abre desempenho de turma própria. O sistema verifica responsabilidade e apresenta lista de atividades, entregas e avaliações. O professor seleciona uma atividade ou estudante. O sistema apresenta os resultados autorizados e resumo de entregas e notas disponíveis, distinguindo ausência de nota.

**Resultado:** Nenhuma avaliação alterada.

**Critério de aceitação:** Resumo coletivo usa somente turma própria e exclui notas não registradas do cálculo da média.

**Restrições:** RN-07, RN-08, RN-16; RNF-01, RNF-08, RNF-10. **Fluxos detalhados:** [CDU-33](../casos-de-uso/M04/CDU-33.md).

##### RF-34 — Manter Comunicado

O sistema deverá oferecer aos atores autorizados a capacidade de publicar, editar e retirar avisos de turmas próprias.

**Atores:** AT-03 · **Origem:** NEC-07 / F-34 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O professor abre comunicados de turma própria. O sistema apresenta formulário de título e texto. O professor preenche e confirma. O sistema registra o comunicado e o apresenta aos participantes autorizados.

**Resultado:** Comunicado criado, editado ou retirado.

**Critério de aceitação:** Participantes da turma veem o aviso; usuários externos à turma não o consultam.

**Restrições:** RN-06; RNF-08, RNF-05, RNF-12. **Fluxos detalhados:** [CDU-34](../casos-de-uso/M04/CDU-34.md).

##### RF-35 — Consultar Comunicados

O sistema deverá oferecer aos atores autorizados a capacidade de visualizar avisos das turmas autorizadas.

**Atores:** AT-08, AT-03 · **Origem:** NEC-07 / F-35 · **Prioridade:** Essencial · **Entrega:** E2 — gestão acadêmica.

**Comportamento principal:** O estudante ou professor abre comunicados de turma acessível. O sistema verifica o vínculo e lista avisos disponíveis. O usuário seleciona um comunicado. O sistema apresenta título, texto, autoria e data.

**Resultado:** Nenhum comunicado é alterado.

**Critério de aceitação:** Aviso privado é acessível somente a participantes autorizados e professor responsável.

**Restrições:** RN-06; RNF-01, RNF-08, RNF-12. **Fluxos detalhados:** [CDU-35](../casos-de-uso/M04/CDU-35.md).

#### M05 — Acessibilidade Linguística

##### RF-36 — Definir Idioma da Interface

O sistema deverá disponibilizar aos atores indicados a opção de selecionar idioma de interface e salvar preferência.

**Atores:** AT-06, AT-10 · **Origem:** NEC-09 / F-36 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre as preferências de idioma. O sistema apresenta idiomas de interface disponíveis. O usuário seleciona um idioma e confirma. O sistema salva a preferência e atualiza os textos fixos da interface.

**Resultado:** Preferência registrada na conta ou no navegador quando visitante.

**Critério de aceitação:** Alternar português/inglês atualiza textos fixos sem traduzir automaticamente conteúdo de usuários.

**Restrições:** Condições gerais da visão; RNF-04, RNF-14, RNF-12. **Fluxos detalhados:** [CDU-36](../casos-de-uso/M05/CDU-36.md).

##### RF-37 — Traduzir Conteúdo Textual

O sistema deverá oferecer aos atores autorizados a capacidade de solicitar tradução de mensagens, publicações, biografias, descrições e trechos textuais elegíveis.

**Atores:** AT-07, AT-05 · **Origem:** NEC-09 / F-37 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona traduzir em conteúdo textual acessível. O sistema apresenta idioma de destino e verifica autorização e elegibilidade do texto. O usuário confirma o idioma. O sistema envia somente texto necessário ao serviço de tradução, recebe o resultado e exibe versão traduzida identificada, com opção de ver original.

**Resultado:** Original inalterado; tradução apresentada como resultado auxiliar.

**Critério de aceitação:** Tradução nunca sobrescreve o original; falha do serviço não impede sua leitura.

**Restrições:** RN-09; RNF-08, RNF-11, RNF-15, RNF-21. **Fluxos detalhados:** [CDU-37](../casos-de-uso/M05/CDU-37.md).

#### M06 — Administração e Moderação

##### RF-38 — Gerenciar Usuários e Acessos

O sistema deverá oferecer aos atores autorizados a capacidade de consultar contas e suspender ou restabelecer acesso conforme autorização.

**Atores:** AT-04 · **Origem:** NEC-10 / F-38 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O administrador abre gestão de contas. O sistema apresenta dados operacionais mínimos, estado e perfil de contas. O administrador seleciona conta e informa motivo da suspensão. O sistema verifica sua autorização, registra a suspensão, revoga sessões da conta e grava a ação em histórico.

**Resultado:** Estado da conta atualizado com registro de ação.

**Critério de aceitação:** Conta suspensa não autentica; gestão não disponibiliza mensagens ou notas privadas.

**Restrições:** RN-01, RN-12; RNF-08, RNF-11, RNF-18. **Fluxos detalhados:** [CDU-38](../casos-de-uso/M06/CDU-38.md).

##### RF-39 — Analisar Solicitação de Perfil Docente

O sistema deverá oferecer aos atores autorizados a capacidade de autorizar ou recusar solicitação com base em critérios de verificação.

**Atores:** AT-04 · **Origem:** NEC-10 / F-39 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O administrador abre solicitações docentes. O sistema apresenta pedidos pendentes e informações de comprovação autorizadas. O administrador seleciona pedido, verifica os critérios e registra decisão de autorizar. O sistema registra a decisão, atribui perfil docente efetivo e apresenta estado ao solicitante.

**Resultado:** Decisão auditável; autorização somente se critérios atendidos.

**Critério de aceitação:** Somente administrador autorizado concede perfil docente; candidato não ganha permissão enquanto pendente.

**Restrições:** RN-01, RN-02, RN-12; RNF-08, RNF-11, RNF-18. **Fluxos detalhados:** [CDU-39](../casos-de-uso/M06/CDU-39.md).

##### RF-40 — Manter Catálogo de Locais

O sistema deverá oferecer aos atores autorizados a capacidade de cadastrar, atualizar e retirar locais recomendados e orientações do guia.

**Atores:** AT-04 · **Origem:** NEC-05 / F-40 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O administrador abre o catálogo de locais e orientações. O sistema apresenta campos de nome, categoria, descrição, localização ou instrução, fonte e data de atualização. O administrador preenche os dados e confirma. O sistema valida campos, registra item e disponibiliza no guia.

**Resultado:** Item cadastrado, atualizado ou retirado.

**Critério de aceitação:** Somente itens ativos do catálogo aparecem no guia; referência e data permitem avaliar atualidade.

**Restrições:** RN-11; RNF-08, RNF-18, RNF-20. **Fluxos detalhados:** [CDU-40](../casos-de-uso/M06/CDU-40.md).

##### RF-41 — Manter Catálogos de Apoio

O sistema deverá oferecer aos atores autorizados a capacidade de manter áreas, interesses, categorias e referências de conteúdo para recomendações.

**Atores:** AT-04 · **Origem:** NEC-06 / F-41 · **Prioridade:** Importante · **Entrega:** E1 — núcleo.

**Comportamento principal:** O administrador abre catálogos de apoio. O sistema apresenta áreas, interesses, categorias e referências de recomendações. O administrador seleciona categoria e cadastra uma referência com título, tema e fonte. O sistema valida unicidade e dados, registra a referência e a torna elegível às recomendações.

**Resultado:** Catálogo atualizado, sem perda indevida de referências existentes.

**Critério de aceitação:** Item inativo deixa de aparecer em novas recomendações; categorias não são duplicadas.

**Restrições:** RN-10, RN-11; RNF-08, RNF-18, RNF-20. **Fluxos detalhados:** [CDU-41](../casos-de-uso/M06/CDU-41.md).

##### RF-42 — Denunciar Conteúdo

O sistema deverá oferecer aos atores autorizados a capacidade de registrar denúncia de conteúdo ou comportamento acessível ao denunciante.

**Atores:** AT-07 · **Origem:** NEC-10 / F-42 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário seleciona denunciar conteúdo ou comportamento que pode acessar. O sistema apresenta categorias e campo para descrição da ocorrência. O usuário informa motivo e confirma. O sistema registra denúncia, referência da evidência necessária e estado pendente, sem divulgar a identidade do denunciante ao denunciado.

**Resultado:** Denúncia pendente registrada.

**Critério de aceitação:** Denúncia válida gera item para moderação e não concede acesso a informações privadas adicionais.

**Restrições:** RN-18; RNF-08, RNF-11, RNF-18. **Fluxos detalhados:** [CDU-42](../casos-de-uso/M06/CDU-42.md).

##### RF-43 — Tratar Denúncias

O sistema deverá oferecer aos atores autorizados a capacidade de analisar evidências autorizadas, registrar decisão e aplicar medidas cabíveis.

**Atores:** AT-04 · **Origem:** NEC-10 / F-43 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O administrador abre a fila de denúncias. O sistema apresenta denúncias pendentes com evidências autorizadas e histórico. O administrador analisa a ocorrência, registra decisão fundamentada e seleciona medida cabível. O sistema aplica a medida permitida, registra a decisão e atualiza o estado da denúncia.

**Resultado:** Denúncia tratada ou mantida pendente; medida e justificativa registradas.

**Critério de aceitação:** Moderação consegue tratar item denunciado sem abrir todas as mensagens privadas ou notas do denunciado.

**Restrições:** RN-04, RN-12, RN-18; RNF-08, RNF-11, RNF-18. **Fluxos detalhados:** [CDU-43](../casos-de-uso/M06/CDU-43.md).

##### RF-44 — Bloquear Usuário

O sistema deverá oferecer aos atores autorizados a capacidade de bloquear usuário, encerrar conexão e impedir novas interações diretas; desfazer bloqueio.

**Atores:** AT-07 · **Origem:** NEC-10 / F-44 · **Prioridade:** Essencial · **Entrega:** E1 — núcleo.

**Comportamento principal:** O usuário abre perfil ou conversa de outro usuário. O sistema apresenta opção de bloqueio. O usuário seleciona bloquear e confirma. O sistema registra bloqueio e impede novos pedidos de conexão e mensagens diretas entre os dois perfis.

**Resultado:** Bloqueio ativo ou removido; conexões anteriores encerradas na ativação.

**Critério de aceitação:** Usuário bloqueado não pode enviar novas mensagens; desbloquear não reativa vínculo automaticamente.

**Restrições:** RN-03, RN-17; RNF-08, RNF-11. **Fluxos detalhados:** [CDU-44](../casos-de-uso/M06/CDU-44.md).

##### RF-45 — Tratar Solicitação de Exclusão de Conta

O sistema deverá oferecer aos atores autorizados a capacidade de executar ou encaminhar tratamento de dados conforme política de retenção.

**Atores:** AT-04 · **Origem:** NEC-10 / F-45 · **Prioridade:** Importante · **Entrega:** E1 — núcleo.

**Comportamento principal:** O administrador abre pedidos de exclusão. O sistema apresenta pedidos pendentes e dados operacionais necessários, sem expor conteúdo privado desnecessário. O administrador verifica identidade, obrigações de retenção e registra decisão de processamento. O sistema encerra acesso, exclui ou anonimiza dados elegíveis, preserva apenas o necessário conforme política validada e registra conclusão.

**Resultado:** Conta encerrada e tratamento registrado, ou pedido permanece pendente.

**Critério de aceitação:** O pedido não é marcado concluído sem processamento efetivo; retenção deve ser justificada.

**Restrições:** RN-12, RN-14; RNF-08, RNF-11, RNF-18, RNF-22. **Fluxos detalhados:** [CDU-45](../casos-de-uso/M06/CDU-45.md).

### 3.3 Requisitos de desempenho, segurança e demais atributos de qualidade

| ID | Categoria | Requisito | Verificação |
| --- | --- | --- | --- |
| RNF-01 | Eficiência de desempenho | Consultas de feed, pessoas, grupos, locais, eventos e turmas devem apresentar até 20 itens por página; em ambiente de referência com 100 usuários simultâneos e 10 mil publicações, 95% das consultas internas devem responder em até 2 s, excluído tempo de transferência de anexos e de serviços externos. | Teste de carga de 10 minutos; medir percentil 95 e paginação. |
| RNF-02 | Eficiência de desempenho | O sistema deve informar estado de processamento de envio de mensagem e confirmar sucesso somente após persistência pelo servidor. | Induzir atraso e falha; conferir indicação e ausência de confirmação falsa. |
| RNF-03 | Flexibilidade | Os fluxos principais devem operar nas versões estáveis de Chrome, Firefox e Edge disponíveis no momento da homologação. | Executar roteiro em cada navegador e registrar versão. |
| RNF-04 | Flexibilidade | Textos fixos da interface devem ser mantidos em recursos de localização separados da lógica; adicionar um idioma não deve exigir alterar regras de negócio. | Inspecionar recursos e adicionar idioma de teste. |
| RNF-05 | Confiabilidade | Registros de notas, entregas, atividades e materiais só devem ser confirmados após persistência; em falha, manter estado anterior ou registrar falha sem sucesso indevido. | Interromper persistência e verificar integridade. |
| RNF-06 | Confiabilidade | Falha no envio de mensagem deve ser indicada; repetir uma mesma solicitação não deve criar mensagens duplicadas. | Simular timeout e repetir identificador de envio. |
| RNF-07 | Segurança | Comunicação entre navegador e servidor deve ocorrer por HTTPS, exceto ambiente local de desenvolvimento. | Inspecionar configuração TLS e redirecionamento de HTTP em homologação. |
| RNF-08 | Segurança | O servidor deve validar autenticação, perfil, autoria e vínculo com turma/grupo em cada operação restrita; permissão negada não retorna dados privados. | Executar requisições diretas com contas sem permissão e sem sessão. |
| RNF-09 | Segurança | Senhas devem ser armazenadas por hash específico para senhas com sal individual, nunca em texto simples; credenciais e tokens não devem aparecer em logs. | Inspecionar armazenamento e logs de teste. |
| RNF-10 | Privacidade | Notas, feedback, entregas e mensagens privadas não devem ser disponibilizados a terceiros sem autorização específica definida. | Testar com dois estudantes, professor de outra turma e administrador. |
| RNF-11 | Privacidade | O cadastro deve informar finalidade e campos opcionais; dados enviados a serviços externos devem ser mínimos e autorizados; e-mail privado não deve ser exposto em perfis. | Inspecionar telas e payloads de teste; conferir aviso e visibilidade. |
| RNF-12 | Capacidade de interação | Telas principais devem se adaptar a 360, 768 e 1920 px sem rolagem horizontal do conteúdo principal. | Testar cada largura no navegador. |
| RNF-13 | Capacidade de interação | Navegação, formulários e ações essenciais devem ser operáveis por teclado, com foco visível, rótulos acessíveis e contraste mínimo de 4,5:1 para texto normal. | Executar teste manual de teclado e verificar contraste. |
| RNF-14 | Capacidade de interação | Os textos fixos das telas principais devem estar disponíveis em português e inglês, sem alterar conteúdo originalmente publicado. | Alternar idioma e conferir menus, botões e mensagens fixas. |
| RNF-15 | Capacidade de interação | Textos traduzidos devem indicar que são traduções automáticas e oferecer opção de ver original; falhas devem manter original acessível. | Solicitar tradução e simular serviço indisponível. |
| RNF-16 | Manutenibilidade | Os seis módulos funcionais devem ter responsabilidades identificáveis, com integração a tradução e e-mail isolada por interfaces de serviço. | Inspecionar arquitetura e substituir adaptador em teste. |
| RNF-17 | Segurança | Tokens de confirmação e recuperação devem ser de uso único e expirar, respectivamente, em até 24 h e 30 min; sessões devem ser invalidadas no logout, redefinição de senha ou suspensão. | Testar token vencido, reutilizado e tentativa de sessão revogada. |
| RNF-18 | Segurança | Ações administrativas e mudanças de nota devem registrar identificador do agente, data, operação, entidade e justificativa quando exigida; o registro não inclui segredos nem conteúdo privado desnecessário. | Executar ação e inspecionar trilha de auditoria. |
| RNF-19 | Segurança / capacidade | Anexos de materiais e entregas devem aceitar PDF, PNG, JPEG e TXT de até 10 MB por arquivo, validar tipo e tamanho no servidor e impedir execução direta de arquivo enviado. | Submeter arquivos válidos, maiores que o limite e de tipo não permitido. |
| RNF-20 | Confiabilidade | Itens de catálogo e divulgações devem registrar origem ou referência quando disponível, data de atualização e estado ativo/retirado. | Criar, atualizar e retirar item; verificar consulta e metadados. |
| RNF-21 | Confiabilidade / desempenho | Se serviço de tradução não responder em até 10 s, o sistema deve informar indisponibilidade, preservar original e permitir nova tentativa. | Simular atraso e erro do serviço. |
| RNF-22 | Privacidade / confiabilidade | O sistema deve permitir registrar o tratamento de pedidos de exclusão e justificativas de retenção; o prazo de retenção será definido em política aprovada antes de implantação com dados reais. | Simular pedido, falha de processamento e conclusão; verificar estado e registro. |

### 3.4 Regras de negócio e restrições

| ID | Regra | Descrição |
| --- | --- | --- |
| RN-01 | A plataforma restringe a concessão de perfis | No cadastro público, o visitante escolhe estudante local, intercambista ou candidato a professor; o perfil administrativo é concedido por procedimento operacional restrito. |
| RN-02 | A administração autoriza o perfil docente | Quando um estudante ou candidato solicita perfil docente, somente administrador autorizado decide após examinar comprovação. Enquanto pendente, o usuário não recebe funções docentes; ao aprovar, o perfil docente torna-se efetivo, sem apagar registros acadêmicos anteriores. Critérios documentais ainda devem ser validados. |
| RN-03 | O destinatário aceita a conexão | Uma conexão só é criada após aceitação do destinatário; novas mensagens diretas exigem conexão ativa e ausência de bloqueio. |
| RN-04 | O autor mantém suas publicações | Somente o autor edita ou exclui publicações e comentários próprios; retirada por moderação constitui ação separada, justificada e registrada. |
| RN-05 | O responsável administra o grupo | O criador ou responsável autorizado gerencia dados e membros do grupo. Grupo aberto admite ingresso direto; grupo restrito exige aprovação do responsável; grupo encerrado não admite novos membros. |
| RN-06 | O professor responsável autoriza o ingresso | O estudante só acessa materiais, atividades e comunicados privados quando possui vínculo ativo com a turma; somente professor responsável autoriza ou revoga participação. |
| RN-07 | A plataforma restringe resultados acadêmicos | Estudante consulta suas próprias entregas, notas e feedback; professor consulta os resultados das turmas sob sua responsabilidade. |
| RN-08 | O UniShare mantém notas internas | Notas são registros internos da plataforma; não equivalem a notas oficiais, matrícula ou histórico institucional. |
| RN-09 | A tradução preserva o original | A tradução é sob demanda, apenas de texto acessível e elegível; original não é sobrescrito. Em falha, continua legível. |
| RN-10 | O sistema recomenda conteúdo por afinidade | Recomendações consideram áreas, interesses e referências ativas; sem dados suficientes, apresenta sugestões gerais ou lista vazia. |
| RN-11 | O responsável mantém os conteúdos de descoberta | Professores mantêm apenas divulgações próprias; administradores mantêm locais, orientações e catálogos de apoio. Itens retirados não aparecem na consulta padrão. |
| RN-12 | A administração registra ações sensíveis | Concessão de perfil, suspensão, moderação e exclusão exigem autorização e registro de ator, instante, motivo e resultado. Não há acesso administrativo irrestrito a notas ou conversas. |
| RN-13 | A plataforma confirma a posse do e-mail | Confirmação e recuperação utilizam tokens de uso único e temporários; posse de e-mail não comprova vínculo docente. Conta não confirmada não inicia sessão. |
| RN-14 | A plataforma trata pedidos de exclusão | Após solicitação confirmada, exclusão ou anonimização respeita retenção justificada e direitos de terceiros; conta é encerrada somente no processamento autorizado. A política de retenção deve ser aprovada antes de uso real. |
| RN-15 | A atividade define o prazo de entrega | Uma atividade possui prazo e pontuação máxima positiva; somente turma ativa e atividade aberta aceitam entrega até o prazo. Substituição, se habilitada, mantém versões anteriores. |
| RN-16 | A avaliação respeita a pontuação da atividade | A nota registrada pertence ao intervalo de zero à pontuação máxima. Atualização exige justificativa; ausência de nota não equivale a zero. Média coletiva considera apenas notas registradas. |
| RN-17 | O bloqueio encerra interações diretas | Bloqueio encerra conexão ativa e pedidos pendentes e impede novas mensagens ou solicitações diretas entre os envolvidos. Histórico previamente autorizado não é apagado; desbloqueio não restaura conexão automaticamente. |
| RN-18 | O denunciante referencia conteúdo acessível | Denúncia registra motivo e evidência acessível ao denunciante; administrador trata apenas dados necessários e identidade do denunciante não é exibida ao denunciado. |
| RN-19 | O usuário controla a visibilidade do perfil | Dados opcionais respeitam configuração de visibilidade; e-mail e dados acadêmicos privados não são publicados por padrão. |
| RN-20 | O sistema restringe arquivos compartilhados | Anexos só são aceitos nos formatos e limites definidos nos RNFs; consulta e download respeitam a mesma autorização do conteúdo. |

### 3.5 Requisitos lógicos de dados

| Entidade | Informações essenciais / restrições |
| --- | --- |
| Conta e perfil | Identificador, e-mail único, estado, perfil efetivo, idioma, preferências de visibilidade; credencial protegida |
| Solicitação docente / exclusão | Solicitante, estado, evidência necessária, decisão, motivo e histórico |
| Conexão, bloqueio e mensagem | Participantes, estado, autoria, conteúdo, data; acesso restrito |
| Publicação, comentário, grupo | Autor, texto, escopo, estado, membros e responsável |
| Local, orientação, evento e referência | Título, categoria, fonte, descrição, datas, estado e autor responsável |
| Turma e vínculo | Professor responsável, estudante, estado do ingresso e período |
| Material, atividade, comunicado | Turma, autoria, conteúdo, estado; atividade tem prazo e pontuação máxima |
| Entrega e avaliação | Estudante, atividade, data, versão, nota, feedback e histórico; acesso individual |
| Denúncia e auditoria | Referência, motivo, estado, agente e decisão; evidência mínima autorizada |

Trata-se de requisitos lógicos, não esquema físico definitivo. Retenção e minimização devem ser validadas antes de implantação real.

### 3.6 Validação e rastreabilidade

Ver [matriz de rastreabilidade](../validacao/matriz-rastreabilidade.md), [revisão de consistência](../validacao/revisao-consistencia.md), [diagramas](../../diagramas-uml/README.md) e [wireframes](../../wireframes/README.md). Os critérios de aceitação são propostas verificáveis para futura implementação. O protótipo demonstra navegação e cenários representativos, sem comprovar os RNFs de produção.
