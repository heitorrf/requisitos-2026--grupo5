# Backlog Priorizado — UniShare

<p align="center"><img src="../docs/assets/logo-unishare.png" alt="Logomarca UniShare" width="360"></p>

**Grupo 5 · Versão 1.0 · 25/11/2026**

> Proposta acadêmica para revisão; não representa validação por usuários reais.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## Critérios de priorização

Essencial: necessário para cumprir o objetivo de um módulo. Importante: agrega valor e admite alternativa temporária. A sequência considera dependências de acesso, governança, comunicação e dados antes dos fluxos que dependem deles. E1 e E2 são recortes conceituais de produto, não sprints acadêmicas. Itens estão especificados como proposta; nenhum é declarado implementado.

## E1 — núcleo

| Ordem | História | Prioridade | RF / CDU | Critério de aceitação |
| --- | --- | --- | --- | --- |
| 1 | Como visitante, quero cadastrar Conta, para criar conta estudantil ou candidatura docente e confirmar e-mail. | Essencial | RF-01 / [CDU-01](../docs/casos-de-uso/M01/CDU-01.md) | Dado um e-mail ainda não cadastrado, ao concluir a confirmação válida, a conta fica ativa; link expirado não ativa a conta. |
| 2 | Como visitante, quero autenticar Usuário, para iniciar sessão com credenciais válidas. | Essencial | RF-02 / [CDU-02](../docs/casos-de-uso/M01/CDU-02.md) | Credenciais válidas de conta ativa abrem sessão; conta não confirmada ou suspensa não entra. |
| 3 | Como visitante, quero recuperar Acesso à Conta, para restabelecer acesso mediante verificação segura. | Essencial | RF-03 / [CDU-03](../docs/casos-de-uso/M01/CDU-03.md) | Token usado, expirado ou inválido não altera senha; token válido permite acesso com a nova senha. |
| 4 | Como usuário autenticado, quero encerrar Sessão, para invalidar a sessão corrente. | Essencial | RF-04 / [CDU-04](../docs/casos-de-uso/M01/CDU-04.md) | Após sair, tentar abrir uma página restrita exige autenticação. |
| 5 | Como usuário acadêmico, quero manter Perfil Acadêmico, para consultar e alterar dados próprios, biografia, instituição, curso ou área, interesses e idiomas. | Essencial | RF-05 / [CDU-05](../docs/casos-de-uso/M01/CDU-05.md) | Alterar a biografia modifica o perfil próprio, mas não permite conceder perfil docente ou administrativo. |
| 6 | Como usuário acadêmico, quero consultar Perfil Acadêmico, para visualizar dados de outro usuário conforme visibilidade. | Essencial | RF-06 / [CDU-06](../docs/casos-de-uso/M01/CDU-06.md) | A consulta não expõe e-mail privado nem informações acadêmicas restritas. |
| 7 | Como estudante, quero solicitar Perfil Docente, para solicitar autorização docente e consultar estado da solicitação. | Essencial | RF-07 / [CDU-07](../docs/casos-de-uso/M01/CDU-07.md) | Uma solicitação pendente não permite criar turmas; decisão de autorização ocorre no CDU-39. |
| 8 | Como administrador, quero analisar Solicitação de Perfil Docente, para autorizar ou recusar solicitação com base em critérios de verificação. | Essencial | RF-39 / [CDU-39](../docs/casos-de-uso/M06/CDU-39.md) | Somente administrador autorizado concede perfil docente; candidato não ganha permissão enquanto pendente. |
| 9 | Como administrador, quero gerenciar Usuários e Acessos, para consultar contas e suspender ou restabelecer acesso conforme autorização. | Essencial | RF-38 / [CDU-38](../docs/casos-de-uso/M06/CDU-38.md) | Conta suspensa não autentica; gestão não disponibiliza mensagens ou notas privadas. |
| 10 | Como visitante, quero definir Idioma da Interface, para selecionar idioma de interface e salvar preferência. | Essencial | RF-36 / [CDU-36](../docs/casos-de-uso/M05/CDU-36.md) | Alternar português/inglês atualiza textos fixos sem traduzir automaticamente conteúdo de usuários. |
| 11 | Como usuário acadêmico, quero pesquisar Usuários, para filtrar pessoas por curso, instituição, área, interesses e idiomas. | Essencial | RF-09 / [CDU-09](../docs/casos-de-uso/M02/CDU-09.md) | Ao filtrar por área e idioma, aparecem somente perfis elegíveis que atendam aos critérios definidos. |
| 12 | Como usuário acadêmico, quero gerenciar Conexões, para enviar, aceitar, recusar, cancelar ou remover conexões. | Essencial | RF-10 / [CDU-10](../docs/casos-de-uso/M02/CDU-10.md) | Uma conexão somente é criada após aceitação do destinatário; bloqueio impede novo pedido. |
| 13 | Como usuário acadêmico, quero bloquear Usuário, para bloquear usuário, encerrar conexão e impedir novas interações diretas; desfazer bloqueio. | Essencial | RF-44 / [CDU-44](../docs/casos-de-uso/M06/CDU-44.md) | Usuário bloqueado não pode enviar novas mensagens; desbloquear não reativa vínculo automaticamente. |
| 14 | Como usuário acadêmico, quero trocar Mensagens, para enviar mensagens entre conexões aceitas e consultar histórico autorizado. | Essencial | RF-11 / [CDU-11](../docs/casos-de-uso/M02/CDU-11.md) | Somente participantes acessam a conversa; envio bloqueado não é armazenado. |
| 15 | Como usuário acadêmico, quero consultar Publicações, para visualizar feed e publicações acessíveis. | Essencial | RF-12 / [CDU-12](../docs/casos-de-uso/M02/CDU-12.md) | Publicações removidas ou de grupo restrito sem participação não aparecem. |
| 16 | Como usuário acadêmico, quero manter Publicação, para criar, editar e excluir publicações próprias no feed ou grupo autorizado. | Essencial | RF-13 / [CDU-13](../docs/casos-de-uso/M02/CDU-13.md) | Usuário publica texto permitido; outro usuário não consegue editar ou excluir a publicação. |
| 17 | Como usuário acadêmico, quero denunciar Conteúdo, para registrar denúncia de conteúdo ou comportamento acessível ao denunciante. | Essencial | RF-42 / [CDU-42](../docs/casos-de-uso/M06/CDU-42.md) | Denúncia válida gera item para moderação e não concede acesso a informações privadas adicionais. |
| 18 | Como administrador, quero tratar Denúncias, para analisar evidências autorizadas, registrar decisão e aplicar medidas cabíveis. | Essencial | RF-43 / [CDU-43](../docs/casos-de-uso/M06/CDU-43.md) | Moderação consegue tratar item denunciado sem abrir todas as mensagens privadas ou notas do denunciado. |
| 19 | Como usuário acadêmico, quero manter Grupo de Estudo, para criar e manter grupos de estudo e gerenciar participantes quando responsável. | Essencial | RF-15 / [CDU-15](../docs/casos-de-uso/M02/CDU-15.md) | Criador pode administrar seu grupo; participante comum não consegue aprovar pedidos de ingresso. |
| 20 | Como usuário acadêmico, quero pesquisar Grupos de Estudo, para localizar grupos por tema ou área. | Essencial | RF-16 / [CDU-16](../docs/casos-de-uso/M02/CDU-16.md) | Busca retorna grupos que correspondem aos filtros, sem revelar publicações restritas. |
| 21 | Como usuário acadêmico, quero participar de Grupo de Estudo, para ingressar, sair e acessar conteúdos do grupo conforme permissões. | Essencial | RF-17 / [CDU-17](../docs/casos-de-uso/M02/CDU-17.md) | Pedido pendente de grupo restrito não concede acesso ao conteúdo privado. |
| 22 | Como administrador, quero manter Catálogo de Locais, para cadastrar, atualizar e retirar locais recomendados e orientações do guia. | Essencial | RF-40 / [CDU-40](../docs/casos-de-uso/M06/CDU-40.md) | Somente itens ativos do catálogo aparecem no guia; referência e data permitem avaliar atualidade. |
| 23 | Como usuário acadêmico, quero consultar Locais Recomendados, para consultar guia de adaptação, orientações, locais de estudo, convivência, serviços e pontos turísticos. | Essencial | RF-18 / [CDU-18](../docs/casos-de-uso/M03/CDU-18.md) | O guia apresenta itens ativos e orientações cadastradas, com filtros por categoria. |
| 24 | Como usuário acadêmico, quero consultar Eventos e Oportunidades, para pesquisar palestras, workshops, congressos, vagas e oportunidades. | Essencial | RF-19 / [CDU-19](../docs/casos-de-uso/M03/CDU-19.md) | Filtro de oportunidades abertas não inclui prazos encerrados; detalhes indicam a fonte fornecida. |
| 25 | Como professor autorizado, quero divulgar Evento ou Oportunidade, para cadastrar, atualizar e retirar divulgações próprias. | Essencial | RF-20 / [CDU-20](../docs/casos-de-uso/M03/CDU-20.md) | Professor divulga evento com período válido; outro professor não pode editar a divulgação sem autorização. |
| 26 | Como usuário acadêmico, quero traduzir Conteúdo Textual, para solicitar tradução de mensagens, publicações, biografias, descrições e trechos textuais elegíveis. | Essencial | RF-37 / [CDU-37](../docs/casos-de-uso/M05/CDU-37.md) | Tradução nunca sobrescreve o original; falha do serviço não impede sua leitura. |
| 27 | Como usuário acadêmico, quero interagir com Publicações, para comentar, reagir e salvar publicações acessíveis; manter interações próprias. | Importante | RF-14 / [CDU-14](../docs/casos-de-uso/M02/CDU-14.md) | Reação pode ser desfeita; salvar não altera a visibilidade para outros usuários. |
| 28 | Como administrador, quero manter Catálogos de Apoio, para manter áreas, interesses, categorias e referências de conteúdo para recomendações. | Importante | RF-41 / [CDU-41](../docs/casos-de-uso/M06/CDU-41.md) | Item inativo deixa de aparecer em novas recomendações; categorias não são duplicadas. |
| 29 | Como usuário acadêmico, quero consultar Recomendações, para receber sugestões de livros, aulas, cursos, conteúdos e eventos por área e interesses. | Importante | RF-21 / [CDU-21](../docs/casos-de-uso/M03/CDU-21.md) | Perfis com áreas distintas recebem sugestões coerentes com as categorias cadastradas. |
| 30 | Como usuário acadêmico, quero solicitar Exclusão de Conta, para solicitar encerramento da conta e tratamento dos dados conforme política aplicável. | Importante | RF-08 / [CDU-08](../docs/casos-de-uso/M01/CDU-08.md) | Cancelar não altera a conta; confirmar gera pedido rastreável para CDU-45. |
| 31 | Como administrador, quero tratar Solicitação de Exclusão de Conta, para executar ou encaminhar tratamento de dados conforme política de retenção. | Importante | RF-45 / [CDU-45](../docs/casos-de-uso/M06/CDU-45.md) | O pedido não é marcado concluído sem processamento efetivo; retenção deve ser justificada. |

## E2 — gestão acadêmica

| Ordem | História | Prioridade | RF / CDU | Critério de aceitação |
| --- | --- | --- | --- | --- |
| 32 | Como professor autorizado, quero manter Turma, para criar, editar e encerrar turmas próprias. | Essencial | RF-22 / [CDU-22](../docs/casos-de-uso/M04/CDU-22.md) | Professor autorizado cria turma; candidato pendente não possui essa permissão. |
| 33 | Como estudante, quero consultar Turmas, para visualizar turmas acessíveis e respectivos dados. | Essencial | RF-23 / [CDU-23](../docs/casos-de-uso/M04/CDU-23.md) | Estudante não inscrito não visualiza materiais privados; professor vê suas turmas. |
| 34 | Como estudante, quero solicitar Participação em Turma, para solicitar ingresso em turma ou cancelar pedido pendente. | Essencial | RF-24 / [CDU-24](../docs/casos-de-uso/M04/CDU-24.md) | Solicitar ingresso não libera materiais; autorização depende do CDU-25. |
| 35 | Como professor autorizado, quero gerenciar Participantes da Turma, para autorizar ou recusar ingresso e gerenciar participantes de turmas próprias. | Essencial | RF-25 / [CDU-25](../docs/casos-de-uso/M04/CDU-25.md) | Somente responsável autorizado decide ingresso; estudante aprovado pode consultar materiais. |
| 36 | Como professor autorizado, quero manter Material Acadêmico, para publicar, atualizar e retirar materiais de turmas próprias. | Essencial | RF-26 / [CDU-26](../docs/casos-de-uso/M04/CDU-26.md) | Aluno autorizado visualiza material; aluno sem vínculo não obtém o arquivo por link direto. |
| 37 | Como estudante, quero consultar Materiais Acadêmicos, para acessar materiais das turmas autorizadas. | Essencial | RF-27 / [CDU-27](../docs/casos-de-uso/M04/CDU-27.md) | A consulta e download respeitam as mesmas permissões da turma. |
| 38 | Como professor autorizado, quero manter Atividade, para criar, atualizar e encerrar tarefas, exercícios e avaliações com prazo. | Essencial | RF-28 / [CDU-28](../docs/casos-de-uso/M04/CDU-28.md) | Atividade com prazo e pontuação válidos é visível aos participantes; encerrada não aceita novas entregas. |
| 39 | Como estudante, quero consultar Atividades, para acessar orientações, prazos e situação das atividades. | Essencial | RF-29 / [CDU-29](../docs/casos-de-uso/M04/CDU-29.md) | Estudante visualiza apenas o estado de sua própria entrega; professor acessa as informações de gestão da turma. |
| 40 | Como estudante, quero submeter Atividade, para entregar trabalho e consultar situação de sua entrega. | Essencial | RF-30 / [CDU-30](../docs/casos-de-uso/M04/CDU-30.md) | Entrega válida dentro do prazo recebe confirmação; fora do prazo é recusada pela regra inicial. |
| 41 | Como professor autorizado, quero avaliar Entregas, para avaliar entregas, atribuir notas dentro da escala da atividade e atualizar feedback. | Essencial | RF-31 / [CDU-31](../docs/casos-de-uso/M04/CDU-31.md) | Nota superior à pontuação máxima é rejeitada; avaliação válida aparece apenas para o aluno avaliado e professor responsável. |
| 42 | Como estudante, quero consultar Desempenho Individual, para acessar notas e feedback próprios. | Essencial | RF-32 / [CDU-32](../docs/casos-de-uso/M04/CDU-32.md) | Usuário não pode obter notas de outro estudante pela interface nem por requisição direta. |
| 43 | Como professor autorizado, quero manter Comunicado, para publicar, editar e retirar avisos de turmas próprias. | Essencial | RF-34 / [CDU-34](../docs/casos-de-uso/M04/CDU-34.md) | Participantes da turma veem o aviso; usuários externos à turma não o consultam. |
| 44 | Como estudante, quero consultar Comunicados, para visualizar avisos das turmas autorizadas. | Essencial | RF-35 / [CDU-35](../docs/casos-de-uso/M04/CDU-35.md) | Aviso privado é acessível somente a participantes autorizados e professor responsável. |
| 45 | Como professor autorizado, quero acompanhar Desempenho da Turma, para consultar resultados individuais e coletivos de turmas próprias. | Importante | RF-33 / [CDU-33](../docs/casos-de-uso/M04/CDU-33.md) | Resumo coletivo usa somente turma própria e exclui notas não registradas do cálculo da média. |

## Gestão das sprints acadêmicas

Consulte [mapa de entregas](entregas-p1-p2.md). Histórias de produto não substituem as issues de entrega do professor. A situação do GitHub Projects não foi alterada.
