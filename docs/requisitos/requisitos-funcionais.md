# Requisitos Funcionais — UniShare

**Grupo 5 · Versão 1.0 · 25/11/2026**

> Proposta acadêmica para revisão; não representa validação por usuários reais.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## Especificação

Cada RF mantém correspondência numérica com a funcionalidade F e o CDU. Os comportamentos completos, alternativas e exceções estão nas especificações individuais. As prioridades são propostas.

### M01 — Identidade e Perfis

| RF | Requisito funcional | Origem | Atores | Prioridade | CDU | Critério de aceitação |
| --- | --- | --- | --- | --- | --- | --- |
| RF-01 | O sistema deverá disponibilizar aos atores indicados a opção de criar conta estudantil ou candidatura docente e confirmar e-mail. | NEC-01 / F-01 | AT-06, AT-09 | Essencial | [CDU-01](../casos-de-uso/M01/CDU-01.md) | Dado um e-mail ainda não cadastrado, ao concluir a confirmação válida, a conta fica ativa; link expirado não ativa a conta. |
| RF-02 | O sistema deverá disponibilizar aos atores indicados a opção de iniciar sessão com credenciais válidas. | NEC-01 / F-02 | AT-06 | Essencial | [CDU-02](../casos-de-uso/M01/CDU-02.md) | Credenciais válidas de conta ativa abrem sessão; conta não confirmada ou suspensa não entra. |
| RF-03 | O sistema deverá disponibilizar aos atores indicados a opção de restabelecer acesso mediante verificação segura. | NEC-01 / F-03 | AT-06, AT-09 | Essencial | [CDU-03](../casos-de-uso/M01/CDU-03.md) | Token usado, expirado ou inválido não altera senha; token válido permite acesso com a nova senha. |
| RF-04 | O sistema deverá oferecer aos atores autorizados a capacidade de invalidar a sessão corrente. | NEC-01 / F-04 | AT-10 | Essencial | [CDU-04](../casos-de-uso/M01/CDU-04.md) | Após sair, tentar abrir uma página restrita exige autenticação. |
| RF-05 | O sistema deverá oferecer aos atores autorizados a capacidade de consultar e alterar dados próprios, biografia, instituição, curso ou área, interesses e idiomas. | NEC-01 / F-05 | AT-07 | Essencial | [CDU-05](../casos-de-uso/M01/CDU-05.md) | Alterar a biografia modifica o perfil próprio, mas não permite conceder perfil docente ou administrativo. |
| RF-06 | O sistema deverá oferecer aos atores autorizados a capacidade de visualizar dados de outro usuário conforme visibilidade. | NEC-01 / F-06 | AT-07 | Essencial | [CDU-06](../casos-de-uso/M01/CDU-06.md) | A consulta não expõe e-mail privado nem informações acadêmicas restritas. |
| RF-07 | O sistema deverá oferecer aos atores autorizados a capacidade de solicitar autorização docente e consultar estado da solicitação. | NEC-10 / F-07 | AT-08, AT-11 | Essencial | [CDU-07](../casos-de-uso/M01/CDU-07.md) | Uma solicitação pendente não permite criar turmas; decisão de autorização ocorre no CDU-39. |
| RF-08 | O sistema deverá oferecer aos atores autorizados a capacidade de solicitar encerramento da conta e tratamento dos dados conforme política aplicável. | NEC-01 / F-08 | AT-07 | Importante | [CDU-08](../casos-de-uso/M01/CDU-08.md) | Cancelar não altera a conta; confirmar gera pedido rastreável para CDU-45. |

### M02 — Rede Social e Comunicação

| RF | Requisito funcional | Origem | Atores | Prioridade | CDU | Critério de aceitação |
| --- | --- | --- | --- | --- | --- | --- |
| RF-09 | O sistema deverá oferecer aos atores autorizados a capacidade de filtrar pessoas por curso, instituição, área, interesses e idiomas. | NEC-02 / F-09 | AT-07 | Essencial | [CDU-09](../casos-de-uso/M02/CDU-09.md) | Ao filtrar por área e idioma, aparecem somente perfis elegíveis que atendam aos critérios definidos. |
| RF-10 | O sistema deverá oferecer aos atores autorizados a capacidade de enviar, aceitar, recusar, cancelar ou remover conexões. | NEC-02 / F-10 | AT-07 | Essencial | [CDU-10](../casos-de-uso/M02/CDU-10.md) | Uma conexão somente é criada após aceitação do destinatário; bloqueio impede novo pedido. |
| RF-11 | O sistema deverá oferecer aos atores autorizados a capacidade de enviar mensagens entre conexões aceitas e consultar histórico autorizado. | NEC-03 / F-11 | AT-07 | Essencial | [CDU-11](../casos-de-uso/M02/CDU-11.md) | Somente participantes acessam a conversa; envio bloqueado não é armazenado. |
| RF-12 | O sistema deverá oferecer aos atores autorizados a capacidade de visualizar feed e publicações acessíveis. | NEC-03 / F-12 | AT-07 | Essencial | [CDU-12](../casos-de-uso/M02/CDU-12.md) | Publicações removidas ou de grupo restrito sem participação não aparecem. |
| RF-13 | O sistema deverá oferecer aos atores autorizados a capacidade de criar, editar e excluir publicações próprias no feed ou grupo autorizado. | NEC-03 / F-13 | AT-07 | Essencial | [CDU-13](../casos-de-uso/M02/CDU-13.md) | Usuário publica texto permitido; outro usuário não consegue editar ou excluir a publicação. |
| RF-14 | O sistema deverá oferecer aos atores autorizados a capacidade de comentar, reagir e salvar publicações acessíveis; manter interações próprias. | NEC-03 / F-14 | AT-07 | Importante | [CDU-14](../casos-de-uso/M02/CDU-14.md) | Reação pode ser desfeita; salvar não altera a visibilidade para outros usuários. |
| RF-15 | O sistema deverá oferecer aos atores autorizados a capacidade de criar e manter grupos de estudo e gerenciar participantes quando responsável. | NEC-04 / F-15 | AT-07 | Essencial | [CDU-15](../casos-de-uso/M02/CDU-15.md) | Criador pode administrar seu grupo; participante comum não consegue aprovar pedidos de ingresso. |
| RF-16 | O sistema deverá oferecer aos atores autorizados a capacidade de localizar grupos por tema ou área. | NEC-04 / F-16 | AT-07 | Essencial | [CDU-16](../casos-de-uso/M02/CDU-16.md) | Busca retorna grupos que correspondem aos filtros, sem revelar publicações restritas. |
| RF-17 | O sistema deverá oferecer aos atores autorizados a capacidade de ingressar, sair e acessar conteúdos do grupo conforme permissões. | NEC-04 / F-17 | AT-07 | Essencial | [CDU-17](../casos-de-uso/M02/CDU-17.md) | Pedido pendente de grupo restrito não concede acesso ao conteúdo privado. |

### M03 — Integração Cultural e Descoberta

| RF | Requisito funcional | Origem | Atores | Prioridade | CDU | Critério de aceitação |
| --- | --- | --- | --- | --- | --- | --- |
| RF-18 | O sistema deverá oferecer aos atores autorizados a capacidade de consultar guia de adaptação, orientações, locais de estudo, convivência, serviços e pontos turísticos. | NEC-05 / F-18 | AT-07 | Essencial | [CDU-18](../casos-de-uso/M03/CDU-18.md) | O guia apresenta itens ativos e orientações cadastradas, com filtros por categoria. |
| RF-19 | O sistema deverá oferecer aos atores autorizados a capacidade de pesquisar palestras, workshops, congressos, vagas e oportunidades. | NEC-05 / F-19 | AT-07 | Essencial | [CDU-19](../casos-de-uso/M03/CDU-19.md) | Filtro de oportunidades abertas não inclui prazos encerrados; detalhes indicam a fonte fornecida. |
| RF-20 | O sistema deverá oferecer aos atores autorizados a capacidade de cadastrar, atualizar e retirar divulgações próprias. | NEC-05 / F-20 | AT-03 | Essencial | [CDU-20](../casos-de-uso/M03/CDU-20.md) | Professor divulga evento com período válido; outro professor não pode editar a divulgação sem autorização. |
| RF-21 | O sistema deverá oferecer aos atores autorizados a capacidade de receber sugestões de livros, aulas, cursos, conteúdos e eventos por área e interesses. | NEC-06 / F-21 | AT-07 | Importante | [CDU-21](../casos-de-uso/M03/CDU-21.md) | Perfis com áreas distintas recebem sugestões coerentes com as categorias cadastradas. |

### M04 — Gestão Acadêmica

| RF | Requisito funcional | Origem | Atores | Prioridade | CDU | Critério de aceitação |
| --- | --- | --- | --- | --- | --- | --- |
| RF-22 | O sistema deverá oferecer aos atores autorizados a capacidade de criar, editar e encerrar turmas próprias. | NEC-07 / F-22 | AT-03 | Essencial | [CDU-22](../casos-de-uso/M04/CDU-22.md) | Professor autorizado cria turma; candidato pendente não possui essa permissão. |
| RF-23 | O sistema deverá oferecer aos atores autorizados a capacidade de visualizar turmas acessíveis e respectivos dados. | NEC-07 / F-23 | AT-08, AT-03 | Essencial | [CDU-23](../casos-de-uso/M04/CDU-23.md) | Estudante não inscrito não visualiza materiais privados; professor vê suas turmas. |
| RF-24 | O sistema deverá oferecer aos atores autorizados a capacidade de solicitar ingresso em turma ou cancelar pedido pendente. | NEC-07 / F-24 | AT-08 | Essencial | [CDU-24](../casos-de-uso/M04/CDU-24.md) | Solicitar ingresso não libera materiais; autorização depende do CDU-25. |
| RF-25 | O sistema deverá oferecer aos atores autorizados a capacidade de autorizar ou recusar ingresso e gerenciar participantes de turmas próprias. | NEC-07 / F-25 | AT-03 | Essencial | [CDU-25](../casos-de-uso/M04/CDU-25.md) | Somente responsável autorizado decide ingresso; estudante aprovado pode consultar materiais. |
| RF-26 | O sistema deverá oferecer aos atores autorizados a capacidade de publicar, atualizar e retirar materiais de turmas próprias. | NEC-07 / F-26 | AT-03 | Essencial | [CDU-26](../casos-de-uso/M04/CDU-26.md) | Aluno autorizado visualiza material; aluno sem vínculo não obtém o arquivo por link direto. |
| RF-27 | O sistema deverá oferecer aos atores autorizados a capacidade de acessar materiais das turmas autorizadas. | NEC-07 / F-27 | AT-08, AT-03 | Essencial | [CDU-27](../casos-de-uso/M04/CDU-27.md) | A consulta e download respeitam as mesmas permissões da turma. |
| RF-28 | O sistema deverá oferecer aos atores autorizados a capacidade de criar, atualizar e encerrar tarefas, exercícios e avaliações com prazo. | NEC-07 / F-28 | AT-03 | Essencial | [CDU-28](../casos-de-uso/M04/CDU-28.md) | Atividade com prazo e pontuação válidos é visível aos participantes; encerrada não aceita novas entregas. |
| RF-29 | O sistema deverá oferecer aos atores autorizados a capacidade de acessar orientações, prazos e situação das atividades. | NEC-07 / F-29 | AT-08, AT-03 | Essencial | [CDU-29](../casos-de-uso/M04/CDU-29.md) | Estudante visualiza apenas o estado de sua própria entrega; professor acessa as informações de gestão da turma. |
| RF-30 | O sistema deverá oferecer aos atores autorizados a capacidade de entregar trabalho e consultar situação de sua entrega. | NEC-08 / F-30 | AT-08 | Essencial | [CDU-30](../casos-de-uso/M04/CDU-30.md) | Entrega válida dentro do prazo recebe confirmação; fora do prazo é recusada pela regra inicial. |
| RF-31 | O sistema deverá oferecer aos atores autorizados a capacidade de avaliar entregas, atribuir notas dentro da escala da atividade e atualizar feedback. | NEC-08 / F-31 | AT-03 | Essencial | [CDU-31](../casos-de-uso/M04/CDU-31.md) | Nota superior à pontuação máxima é rejeitada; avaliação válida aparece apenas para o aluno avaliado e professor responsável. |
| RF-32 | O sistema deverá oferecer aos atores autorizados a capacidade de acessar notas e feedback próprios. | NEC-08 / F-32 | AT-08 | Essencial | [CDU-32](../casos-de-uso/M04/CDU-32.md) | Usuário não pode obter notas de outro estudante pela interface nem por requisição direta. |
| RF-33 | O sistema deverá oferecer aos atores autorizados a capacidade de consultar resultados individuais e coletivos de turmas próprias. | NEC-08 / F-33 | AT-03 | Importante | [CDU-33](../casos-de-uso/M04/CDU-33.md) | Resumo coletivo usa somente turma própria e exclui notas não registradas do cálculo da média. |
| RF-34 | O sistema deverá oferecer aos atores autorizados a capacidade de publicar, editar e retirar avisos de turmas próprias. | NEC-07 / F-34 | AT-03 | Essencial | [CDU-34](../casos-de-uso/M04/CDU-34.md) | Participantes da turma veem o aviso; usuários externos à turma não o consultam. |
| RF-35 | O sistema deverá oferecer aos atores autorizados a capacidade de visualizar avisos das turmas autorizadas. | NEC-07 / F-35 | AT-08, AT-03 | Essencial | [CDU-35](../casos-de-uso/M04/CDU-35.md) | Aviso privado é acessível somente a participantes autorizados e professor responsável. |

### M05 — Acessibilidade Linguística

| RF | Requisito funcional | Origem | Atores | Prioridade | CDU | Critério de aceitação |
| --- | --- | --- | --- | --- | --- | --- |
| RF-36 | O sistema deverá disponibilizar aos atores indicados a opção de selecionar idioma de interface e salvar preferência. | NEC-09 / F-36 | AT-06, AT-10 | Essencial | [CDU-36](../casos-de-uso/M05/CDU-36.md) | Alternar português/inglês atualiza textos fixos sem traduzir automaticamente conteúdo de usuários. |
| RF-37 | O sistema deverá oferecer aos atores autorizados a capacidade de solicitar tradução de mensagens, publicações, biografias, descrições e trechos textuais elegíveis. | NEC-09 / F-37 | AT-07, AT-05 | Essencial | [CDU-37](../casos-de-uso/M05/CDU-37.md) | Tradução nunca sobrescreve o original; falha do serviço não impede sua leitura. |

### M06 — Administração e Moderação

| RF | Requisito funcional | Origem | Atores | Prioridade | CDU | Critério de aceitação |
| --- | --- | --- | --- | --- | --- | --- |
| RF-38 | O sistema deverá oferecer aos atores autorizados a capacidade de consultar contas e suspender ou restabelecer acesso conforme autorização. | NEC-10 / F-38 | AT-04 | Essencial | [CDU-38](../casos-de-uso/M06/CDU-38.md) | Conta suspensa não autentica; gestão não disponibiliza mensagens ou notas privadas. |
| RF-39 | O sistema deverá oferecer aos atores autorizados a capacidade de autorizar ou recusar solicitação com base em critérios de verificação. | NEC-10 / F-39 | AT-04 | Essencial | [CDU-39](../casos-de-uso/M06/CDU-39.md) | Somente administrador autorizado concede perfil docente; candidato não ganha permissão enquanto pendente. |
| RF-40 | O sistema deverá oferecer aos atores autorizados a capacidade de cadastrar, atualizar e retirar locais recomendados e orientações do guia. | NEC-05 / F-40 | AT-04 | Essencial | [CDU-40](../casos-de-uso/M06/CDU-40.md) | Somente itens ativos do catálogo aparecem no guia; referência e data permitem avaliar atualidade. |
| RF-41 | O sistema deverá oferecer aos atores autorizados a capacidade de manter áreas, interesses, categorias e referências de conteúdo para recomendações. | NEC-06 / F-41 | AT-04 | Importante | [CDU-41](../casos-de-uso/M06/CDU-41.md) | Item inativo deixa de aparecer em novas recomendações; categorias não são duplicadas. |
| RF-42 | O sistema deverá oferecer aos atores autorizados a capacidade de registrar denúncia de conteúdo ou comportamento acessível ao denunciante. | NEC-10 / F-42 | AT-07 | Essencial | [CDU-42](../casos-de-uso/M06/CDU-42.md) | Denúncia válida gera item para moderação e não concede acesso a informações privadas adicionais. |
| RF-43 | O sistema deverá oferecer aos atores autorizados a capacidade de analisar evidências autorizadas, registrar decisão e aplicar medidas cabíveis. | NEC-10 / F-43 | AT-04 | Essencial | [CDU-43](../casos-de-uso/M06/CDU-43.md) | Moderação consegue tratar item denunciado sem abrir todas as mensagens privadas ou notas do denunciado. |
| RF-44 | O sistema deverá oferecer aos atores autorizados a capacidade de bloquear usuário, encerrar conexão e impedir novas interações diretas; desfazer bloqueio. | NEC-10 / F-44 | AT-07 | Essencial | [CDU-44](../casos-de-uso/M06/CDU-44.md) | Usuário bloqueado não pode enviar novas mensagens; desbloquear não reativa vínculo automaticamente. |
| RF-45 | O sistema deverá oferecer aos atores autorizados a capacidade de executar ou encaminhar tratamento de dados conforme política de retenção. | NEC-10 / F-45 | AT-04 | Importante | [CDU-45](../casos-de-uso/M06/CDU-45.md) | O pedido não é marcado concluído sem processamento efetivo; retenção deve ser justificada. |

[Visão](../01-visao-demanda.md) · [Regras de negócio](regras-de-negocio.md) · [SRS](../srs/SRS-UniShare-v1.0.md)
