# Requisitos Não Funcionais — UniShare

**Grupo 5 · Versão 1.0 · 25/11/2026**

> Proposta acadêmica para revisão; não representa validação por usuários reais.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| --- | --- | --- | --- |
| 25/11/2026 | 1.0 | Consolidação e alinhamento com a visão 4.0 | Grupo 5 — proposta |

## 1. Requisitos de produto

Os limites quantitativos são metas de especificação propostas, não medições. O protótipo estático não comprova desempenho, segurança ou persistência de um sistema real.

### 1.1 Eficiência de desempenho

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-01 | Consultas de feed, pessoas, grupos, locais, eventos e turmas devem apresentar até 20 itens por página; em ambiente de referência com 100 usuários simultâneos e 10 mil publicações, 95% das consultas internas devem responder em até 2 s, excluído tempo de transferência de anexos e de serviços externos. | Teste de carga de 10 minutos; medir percentil 95 e paginação. | Proposto; validar carga e ambiente. |
| RNF-02 | O sistema deve informar estado de processamento de envio de mensagem e confirmar sucesso somente após persistência pelo servidor. | Induzir atraso e falha; conferir indicação e ausência de confirmação falsa. | Proposto. |

### 1.2 Flexibilidade

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-03 | Os fluxos principais devem operar nas versões estáveis de Chrome, Firefox e Edge disponíveis no momento da homologação. | Executar roteiro em cada navegador e registrar versão. | Proposto. |
| RNF-04 | Textos fixos da interface devem ser mantidos em recursos de localização separados da lógica; adicionar um idioma não deve exigir alterar regras de negócio. | Inspecionar recursos e adicionar idioma de teste. | Proposto. |

### 1.3 Confiabilidade

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-05 | Registros de notas, entregas, atividades e materiais só devem ser confirmados após persistência; em falha, manter estado anterior ou registrar falha sem sucesso indevido. | Interromper persistência e verificar integridade. | Proposto. |
| RNF-06 | Falha no envio de mensagem deve ser indicada; repetir uma mesma solicitação não deve criar mensagens duplicadas. | Simular timeout e repetir identificador de envio. | Proposto. |
| RNF-20 | Itens de catálogo e divulgações devem registrar origem ou referência quando disponível, data de atualização e estado ativo/retirado. | Criar, atualizar e retirar item; verificar consulta e metadados. | Proposto. |
| RNF-21 | Se serviço de tradução não responder em até 10 s, o sistema deve informar indisponibilidade, preservar original e permitir nova tentativa. | Simular atraso e erro do serviço. | Proposto; timeout a validar. |

### 1.4 Segurança

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-07 | Comunicação entre navegador e servidor deve ocorrer por HTTPS, exceto ambiente local de desenvolvimento. | Inspecionar configuração TLS e redirecionamento de HTTP em homologação. | Proposto. |
| RNF-08 | O servidor deve validar autenticação, perfil, autoria e vínculo com turma/grupo em cada operação restrita; permissão negada não retorna dados privados. | Executar requisições diretas com contas sem permissão e sem sessão. | Proposto. |
| RNF-09 | Senhas devem ser armazenadas por hash específico para senhas com sal individual, nunca em texto simples; credenciais e tokens não devem aparecer em logs. | Inspecionar armazenamento e logs de teste. | Proposto. |
| RNF-17 | Tokens de confirmação e recuperação devem ser de uso único e expirar, respectivamente, em até 24 h e 30 min; sessões devem ser invalidadas no logout, redefinição de senha ou suspensão. | Testar token vencido, reutilizado e tentativa de sessão revogada. | Proposto; prazos a validar. |
| RNF-18 | Ações administrativas e mudanças de nota devem registrar identificador do agente, data, operação, entidade e justificativa quando exigida; o registro não inclui segredos nem conteúdo privado desnecessário. | Executar ação e inspecionar trilha de auditoria. | Proposto. |
| RNF-19 | Anexos de materiais e entregas devem aceitar PDF, PNG, JPEG e TXT de até 10 MB por arquivo, validar tipo e tamanho no servidor e impedir execução direta de arquivo enviado. | Submeter arquivos válidos, maiores que o limite e de tipo não permitido. | Proposto; limites a validar. |

### 1.5 Privacidade

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-10 | Notas, feedback, entregas e mensagens privadas não devem ser disponibilizados a terceiros sem autorização específica definida. | Testar com dois estudantes, professor de outra turma e administrador. | Proposto. |
| RNF-11 | O cadastro deve informar finalidade e campos opcionais; dados enviados a serviços externos devem ser mínimos e autorizados; e-mail privado não deve ser exposto em perfis. | Inspecionar telas e payloads de teste; conferir aviso e visibilidade. | Proposto; política pendente. |
| RNF-22 | O sistema deve permitir registrar o tratamento de pedidos de exclusão e justificativas de retenção; o prazo de retenção será definido em política aprovada antes de implantação com dados reais. | Simular pedido, falha de processamento e conclusão; verificar estado e registro. | Dependente de política; não validado. |

### 1.6 Capacidade de interação

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-12 | Telas principais devem se adaptar a 360, 768 e 1920 px sem rolagem horizontal do conteúdo principal. | Testar cada largura no navegador. | Proposto. |
| RNF-13 | Navegação, formulários e ações essenciais devem ser operáveis por teclado, com foco visível, rótulos acessíveis e contraste mínimo de 4,5:1 para texto normal. | Executar teste manual de teclado e verificar contraste. | Proposto. |
| RNF-14 | Os textos fixos das telas principais devem estar disponíveis em português e inglês, sem alterar conteúdo originalmente publicado. | Alternar idioma e conferir menus, botões e mensagens fixas. | Proposto; idiomas a validar. |
| RNF-15 | Textos traduzidos devem indicar que são traduções automáticas e oferecer opção de ver original; falhas devem manter original acessível. | Solicitar tradução e simular serviço indisponível. | Proposto. |

### 1.7 Manutenibilidade

| ID | Requisito e critério | Verificação | Estado |
| --- | --- | --- | --- |
| RNF-16 | Os seis módulos funcionais devem ter responsabilidades identificáveis, com integração a tradução e e-mail isolada por interfaces de serviço. | Inspecionar arquitetura e substituir adaptador em teste. | Proposto. |

## 2. Requisitos organizacionais e externos

Ambiente inicial: aplicação web, documentação versionada no GitHub e protótipo local/estático para apresentação. A integração com provedores depende de viabilidade, contrato e avaliação de privacidade. Nenhuma instituição foi autorizada a compartilhar dados reais. As condições legais e prazos de retenção permanecem pendentes.

## 3. Validação

- [x] Categorias relevantes e critérios verificáveis identificados.
- [x] Referências aos CDUs na matriz de rastreabilidade.
- [ ] Metas de carga, limites de arquivos, idiomas e prazos homologados.
- [ ] Testes de sistema real realizados.
- [ ] Revisão de privacidade e validação com usuários.
