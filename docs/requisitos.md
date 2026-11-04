# Especificação de Requisitos

**Projeto:** Rede Social Acadêmica Internacional  
**Grupo:** 5  
**Versão:** 1.0  
**Artefato:** Especificação de Requisitos Funcionais e Não Funcionais

## 1. Apresentação

Este documento especifica os requisitos da **Rede Social Acadêmica Internacional**, uma plataforma web voltada à integração entre estudantes intercambistas, estudantes locais e professores. A proposta reúne comunicação, colaboração acadêmica, informações para adaptação ao campus e acompanhamento de atividades educacionais, com recursos de interface multilíngue e tradução de conteúdos.

Os **requisitos funcionais (RF)** descrevem as funcionalidades previstas. Os **requisitos não funcionais (RNF)** estabelecem condições de qualidade e restrições aplicáveis à solução. Ambos utilizam identificadores únicos para facilitar a consulta e a relação com os demais artefatos do projeto.

## 2. Requisitos funcionais

### 2.1. Acesso, perfis e conexões

| ID | Requisito funcional |
|---|---|
| **RF01** | O sistema deverá permitir que estudantes e professores se autentiquem para acessar suas contas. |
| **RF02** | O sistema deverá permitir que o usuário crie e atualize seu perfil acadêmico, incluindo instituição, curso ou área de atuação e interesses. |
| **RF03** | O sistema deverá permitir a busca de perfis de estudantes por curso, área de conhecimento e interesses, incluindo a identificação de estudantes locais para integração com intercambistas. |
| **RF04** | O sistema deverá permitir que estudantes enviem solicitações de conexão acadêmica e que seus destinatários as aceitem ou recusem. |

### 2.2. Comunicação e comunidades

| ID | Requisito funcional |
|---|---|
| **RF05** | O sistema deverá permitir a troca de mensagens entre usuários. |
| **RF06** | O sistema deverá permitir que usuários consultem e participem de grupos de estudo e comunidades acadêmicas. |
| **RF07** | O sistema deverá permitir que usuários criem, consultem e compartilhem publicações e materiais acadêmicos. |

### 2.3. Integração e recomendações

| ID | Requisito funcional |
|---|---|
| **RF08** | O sistema deverá disponibilizar guias e informações de adaptação ao campus para estudantes intercambistas. |
| **RF09** | O sistema deverá permitir a consulta de eventos acadêmicos, locais de estudo, pontos turísticos e espaços de convivência recomendados. |
| **RF10** | O sistema deverá permitir a filtragem de conteúdos e eventos por área de conhecimento ou interesse acadêmico. |

### 2.4. Gestão acadêmica

| ID | Requisito funcional |
|---|---|
| **RF11** | O sistema deverá permitir que estudantes consultem suas atividades, seus prazos e suas notas. |
| **RF12** | O sistema deverá permitir que professores criem e atualizem atividades acadêmicas e seus prazos. |
| **RF13** | O sistema deverá permitir que professores publiquem materiais didáticos e comunicados para suas turmas. |
| **RF14** | O sistema deverá permitir que professores registrem e atualizem notas dos estudantes. |
| **RF15** | O sistema deverá permitir que professores consultem o desempenho acadêmico dos estudantes de suas turmas. |

### 2.5. Idioma e tradução

| ID | Requisito funcional |
|---|---|
| **RF16** | O sistema deverá permitir que o usuário selecione o idioma da interface entre as opções disponíveis. |
| **RF17** | O sistema deverá permitir que o usuário solicite a tradução de textos exibidos na plataforma, incluindo mensagens, publicações, biografias, descrições e guias, para um idioma disponível. |

## 3. Requisitos não funcionais

Os RNFs estão organizados segundo as sete categorias essenciais indicadas no modelo LAPIS. A coluna **Verificação** apresenta um procedimento objetivo para avaliar o atendimento de cada requisito.

### 3.1. Eficiência de desempenho

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF01** | As operações de consulta a perfis, grupos e eventos deverão informar o usuário quando uma requisição estiver em processamento, até a apresentação do resultado ou de uma mensagem de falha. | Simular consultas com diferentes tempos de resposta e verificar a indicação de processamento e o encerramento desse estado. |
| **RNF02** | O envio de mensagens não deverá apresentar confirmação de sucesso antes do recebimento da confirmação de registro pelo servidor. | Simular atrasos e falhas no envio e verificar o momento em que a confirmação é exibida. |

### 3.2. Flexibilidade

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF03** | As funcionalidades principais da plataforma deverão operar nas versões estáveis atuais dos navegadores Chrome, Firefox e Edge. | Executar os mesmos cenários de acesso, navegação, mensagens e consulta acadêmica nos três navegadores. |
| **RNF04** | Os textos fixos da interface deverão ser armazenados em recursos de localização separados da lógica das funcionalidades. | Inspecionar a organização da aplicação e verificar se um texto da interface pode ser alterado sem modificar a lógica funcional. |

### 3.3. Confiabilidade

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF05** | O sistema não deverá confirmar o registro de notas ou atividades antes da conclusão de seu armazenamento. | Simular falha durante o armazenamento e verificar que não há confirmação indevida. |
| **RNF06** | Quando o envio de uma mensagem não for confirmado pelo servidor, o sistema deverá informar a falha ao remetente. | Interromper a comunicação durante o envio e verificar a mensagem apresentada ao usuário. |

### 3.4. Segurança

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF07** | A comunicação entre o navegador e o servidor deverá ocorrer por HTTPS. | Inspecionar as conexões realizadas durante os principais fluxos da plataforma. |
| **RNF08** | O servidor deverá verificar a autenticação e a autorização do usuário antes de executar operações restritas sobre perfis e dados acadêmicos. | Tentar executar operações restritas sem autenticação e com contas sem a permissão correspondente. |
| **RNF09** | As senhas de usuários não poderão ser armazenadas em texto simples; deverá ser empregado um mecanismo de hash específico para senhas, com sal individual. | Inspecionar a implementação de autenticação e o armazenamento das credenciais. |

### 3.5. Privacidade

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF10** | As notas individuais de um estudante não deverão ser expostas a outros estudantes por meio das telas ou das respostas da aplicação. | Tentar acessar notas de outro estudante pela interface e por requisições diretas. |
| **RNF11** | O cadastro deverá apresentar ao usuário as finalidades de uso dos dados pessoais solicitados antes do envio das informações. | Inspecionar o fluxo de cadastro e verificar a apresentação dessas informações. |

### 3.6. Capacidade de interação

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF12** | As telas principais deverão se adaptar a larguras de visualização entre 360 e 1920 pixels sem rolagem horizontal para a leitura do conteúdo principal. | Verificar as telas principais em larguras dentro do intervalo definido. |
| **RNF13** | As funções principais de navegação, mensagens e consulta acadêmica deverão ser operáveis por teclado, com indicação visível do foco. | Executar esses fluxos sem mouse e verificar a identificação do elemento selecionado. |
| **RNF14** | Após a seleção de um idioma disponível, os textos fixos da interface deverão ser apresentados nesse idioma nas telas principais. | Alternar o idioma e conferir menus, botões, títulos e mensagens da interface. |
| **RNF15** | Os conteúdos exibidos por tradução automática deverão ser identificados como traduzidos e permitir a visualização do texto original. | Solicitar traduções de mensagens, publicações e descrições e verificar a identificação e o acesso ao original. |

### 3.7. Manutenibilidade

| ID | Requisito não funcional | Verificação |
|---|---|---|
| **RNF16** | A implementação deverá organizar perfis, comunicação, comunidades, gestão acadêmica e internacionalização em módulos com responsabilidades identificáveis. | Inspecionar a estrutura do código e verificar a separação das responsabilidades. |

## 4. Relação com os demais artefatos

Os requisitos foram organizados para manter correspondência com o Documento de Visão, os casos de uso e as regras de negócio do Grupo 5. A tabela apresenta as principais relações, sem substituir a descrição detalhada desses artefatos.

| Requisitos | Casos de uso ou funcionalidades relacionadas | Regras de negócio relacionadas |
|---|---|---|
| **RF01–RF02** | Acesso à plataforma; Gerenciar perfil acadêmico | RN01 |
| **RF03–RF04** | Buscar estudantes por curso e interesses; Encontrar estudantes locais para integração; Criar conexões acadêmicas | RN02 |
| **RF05–RF07** | Trocar mensagens; Participar de grupos de estudo; Compartilhar publicações e materiais | RN03, RN04 |
| **RF08–RF10** | Consultar guia de adaptação ao campus; Consultar eventos e locais recomendados; filtragem por área de conhecimento | RN11, RN12 |
| **RF11–RF15** | Consultar atividades, prazos e notas; Gerenciar atividades e prazos; Publicar materiais e comunicados; Registrar notas e acompanhar desempenho | RN05–RN08 |
| **RF16–RF17** | Selecionar idioma da interface; Traduzir conteúdo textual sob demanda | RN09, RN10 |
| **RNF07–RNF11** | Proteção do acesso e dos dados acadêmicos | RN01, RN05–RN08 |
| **RNF14–RNF15** | Selecionar idioma da interface; Traduzir conteúdo textual sob demanda | RN09, RN10 |

**Documentos relacionados:**

- **Documento de Visão:** objetivos, públicos e escopo da plataforma.
- **Diagrama de Casos de Uso:** interações previstas entre usuários e sistema.
- **Diagrama de Componentes:** organização lógica dos módulos e dos serviços de internacionalização.
- **Diagrama de Implantação:** infraestrutura proposta para a aplicação web.
- **Especificação de Regras de Negócio:** condições de autoria, autorização, acesso e tratamento de conteúdos.

---

**Grupo 5 — Rede Social Acadêmica Internacional**
