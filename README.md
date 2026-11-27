# Conhecimento em Docker

Repositório de estudos práticos sobre **Docker, conteinerização, redes, persistência de dados, Docker Compose e Kubernetes**. O conteúdo reúne exercícios independentes que demonstram, de forma progressiva, como empacotar aplicações, executar containers, conectar serviços e definir recursos de orquestração.

Os exemplos utilizam aplicações desenvolvidas com Python, JavaScript e PHP, além de serviços de banco de dados. Cada diretório apresenta um cenário específico, permitindo estudar diferentes configurações e comparar abordagens.

## Objetivo do projeto

Consolidar conhecimentos sobre conteinerização e orquestração por meio de exemplos práticos e configurações executáveis, explorando:

- Construção de imagens Docker por meio de Dockerfiles.
- Criação e execução de containers.
- Mapeamento e exposição de portas.
- Persistência de arquivos e dados com volumes e bind mounts.
- Comunicação entre containers, host e serviços externos.
- Organização de múltiplos serviços com Docker Compose.
- Configuração de aplicações com arquivos YAML e variáveis de ambiente.
- Definição de Deployments e Services no Kubernetes.
- Conteinerização de aplicações web e APIs com Flask, FastAPI, Express e PHP.

## Stack tecnológica

| Categoria | Tecnologia | Aplicação no repositório |
|---|---|---|
| Conteinerização | Docker e Dockerfile | Construção de imagens, configuração do ambiente, instalação de dependências e inicialização de aplicações. |
| Composição de serviços | Docker Compose | Definição de serviços, redes, volumes, variáveis de ambiente e dependências entre containers. |
| Orquestração | Kubernetes | Configuração declarativa de Deployments, Services, réplicas e exposição de aplicações. |
| Linguagem | Python | Desenvolvimento de aplicações web, APIs e integração com serviços externos e banco de dados. |
| Frameworks Python | Flask e FastAPI | Criação de rotas HTTP, respostas JSON e páginas web. |
| Servidor ASGI | Uvicorn | Execução das aplicações desenvolvidas com FastAPI. |
| JavaScript | Node.js e Express | Desenvolvimento de aplicações HTTP e APIs com rotas e respostas JSON. |
| Banco de dados | MySQL 5.7 | Persistência relacional e comunicação entre aplicações e containers. |
| Integração HTTP | Requests | Consumo de serviços externos a partir de aplicações Python. |
| Integração com MySQL | Flask-MySQLdb | Conexão das aplicações Flask com o banco de dados. |
| Aplicação web | PHP e Apache | Desenvolvimento de formulário web e gravação de informações em arquivos. |
| Configuração | YAML e arquivos `.env` | Organização de parâmetros, serviços e manifests de infraestrutura. |
| Versionamento | Git | Organização dos arquivos do projeto e controle de versões. |

## Estrutura do projeto

A estrutura está organizada por assunto e cenário de estudo. Os diretórios agrupam exemplos independentes, desde a criação de imagens até a comunicação entre serviços e a configuração de recursos Kubernetes.

```text
.
├── Imagem/
│   ├── Dockerfile
│   ├── app.js
│   ├── package.json
│   └── package-lock.json
├── Projetos/
│   ├── 0409/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   └── project0409.yaml
│   └── 1809/
│       ├── Dockerfile
│       └── api.js
├── compose/
│   ├── bind_mount/
│   │   ├── config/
│   │   ├── docker-compose.yaml
│   │   ├── flask/
│   │   └── mysql/
│   ├── criacao_compose/
│   │   └── docker-compose.yaml
│   ├── network/
│   │   ├── config/
│   │   └── docker-compose.yaml
│   ├── projeto/
│   │   ├── config/
│   │   ├── docker-compose.yaml
│   │   ├── flask/
│   │   └── mysql/
│   └── variaveis/
│       ├── config/
│       └── docker-compose.yaml
├── copia/
│   └── app.js
├── kubernetes/
│   ├── 1_projeto/
│   ├── 2_modo_declarativo/
│   └── 3_uniao_arqs/
├── network/
│   ├── 1_externa/
│   ├── 2_host/
│   └── 3_conn_containers/
├── teste/
│   ├── dockerfile
│   └── main.py
├── volumes/
│   ├── Dockerfile
│   ├── index.php
│   ├── process.php
│   └── messages/
└── yaml/
    ├── app.py
    └── test.yaml
```

### Arquivos da raiz

| Arquivo | Descrição |
|---|---|
| `README.md` | Documentação do repositório e orientação sobre os exercícios. |
| `Definicoes.txt` | Anotações de estudo sobre comandos e conceitos de Docker, volumes, redes, Compose, Swarm e Kubernetes. |
| `.gitignore` | Configuração de arquivos e diretórios ignorados pelo Git. |
| `.gitattributes` | Configuração de atributos e normalização de arquivos de texto. |

### `Imagem/` — Construção de imagem com Node.js

Contém uma aplicação simples desenvolvida com Node.js e Express, utilizada para estudar a construção de imagens Docker.

- `Dockerfile`: define a imagem base, configura o diretório de trabalho, instala dependências, copia os arquivos e inicia a aplicação.
- `app.js`: implementa as rotas `/` e `/hello-world`, com respostas em texto.
- `package.json`: descreve as dependências e configurações do projeto.
- `package-lock.json`: registra as versões resolvidas das dependências instaladas pelo npm.

**Conhecimentos aplicados:** Dockerfile, imagens, containers, Node.js, Express, gerenciamento de dependências e exposição de portas.

### `Projetos/` — Aplicações e manifests Kubernetes

Agrupa dois exercícios de desenvolvimento de aplicações conteinerizadas.

**`Projetos/0409/`**

Aplicação desenvolvida com FastAPI, com endpoints `/` e `/lista_funcionarios`, executada pelo Uvicorn na porta 8080.

- `Dockerfile`: configura o ambiente Python e instala FastAPI e Uvicorn.
- `app.py`: implementa os endpoints da aplicação.
- `project0409.yaml`: define um Deployment Kubernetes com quatro réplicas e um Service do tipo `LoadBalancer`.

**`Projetos/1809/`**

API desenvolvida com Node.js e Express.

- `Dockerfile`: utiliza Node 20.14, instala o Express e configura a inicialização da aplicação.
- `api.js`: implementa as rotas `/`, `/api` e `/api/users`, com respostas JSON.

**Conhecimentos aplicados:** FastAPI, Uvicorn, Node.js, Express, construção de imagens e configuração de recursos Kubernetes.

### `compose/` — Composição de serviços

Reúne exemplos de Docker Compose que demonstram diferentes formas de organizar aplicações compostas por múltiplos containers.

**`compose/criacao_compose/`**

Configuração de WordPress e MySQL. O banco utiliza a imagem `mysql:5.7` e um volume nomeado `db_data` para persistência. O WordPress é publicado na porta 8000 do host.

**`compose/variaveis/`**

Variação do cenário WordPress com MySQL, organizando parâmetros de configuração nos arquivos `config/db.env` e `config/wp.env`. Também utiliza volume nomeado para os dados do banco.

**`compose/network/`**

Configura WordPress e MySQL em uma rede bridge chamada `backend`. Demonstra a declaração explícita de rede, a separação de variáveis de ambiente e a persistência dos dados do banco.

**`compose/projeto/`**

Composição de uma aplicação Flask e um banco MySQL em uma rede Docker chamada `dockercompose`.

- `flask/app.py`: realiza chamadas à API externa `randomuser.me` e disponibiliza uma rota que grava o nome retornado no MySQL.
- `mysql/schema.sql`: cria o banco `flaskdocker` e a tabela `users`.
- `config/db.env`: reúne parâmetros de configuração do banco.

**`compose/bind_mount/`**

Adaptação do cenário Flask e MySQL, utilizando bind mount para compartilhar o código da aplicação entre o host e o container.

- `flask/`: contém o Dockerfile e a aplicação Flask.
- `mysql/`: contém o Dockerfile e o script SQL de criação do banco e da tabela.
- `config/`: reúne as variáveis de configuração do banco.
- `docker-compose.yaml`: define os serviços e o mapeamento do diretório da aplicação.

**Conhecimentos aplicados:** Docker Compose, múltiplos serviços, redes bridge, volumes nomeados, bind mounts, variáveis de ambiente, dependências entre containers e integração entre Flask e MySQL.

### `copia/` — Exemplo de aplicação Express

Contém uma cópia do arquivo `app.js` utilizado no exemplo de `Imagem/`, permitindo consultar a implementação da aplicação Express de forma isolada.

### `kubernetes/` — Configuração declarativa e orquestração

Organiza os exercícios de Kubernetes em etapas, demonstrando a evolução da configuração de uma aplicação Flask.

**`kubernetes/1_projeto/`**

- `app.py`: aplicação Flask que renderiza a página `templates/index.html`.
- `dockerfile`: define a construção da imagem da aplicação.
- `templates/index.html`: interface HTML renderizada pela aplicação.

**`kubernetes/2_modo_declarativo/`**

Apresenta os recursos Kubernetes em arquivos separados.

- `app.py`, `dockerfile` e `templates/`: implementação da aplicação Flask.
- `flask.yaml`: define um Deployment com quatro réplicas.
- `flask-service.yaml`: define um Service do tipo `LoadBalancer`, selecionando os pods por meio de labels.

**`kubernetes/3_uniao_arqs/`**

Reúne os recursos de Deployment e Service em um único arquivo YAML.

- `app.py`: aplicação Flask.
- `dockerfile`: configuração da imagem.
- `templates/index.html`: página da aplicação.
- `flask-project.yaml`: reúne Deployment e Service, separados pelo delimitador `---`. O Deployment configura quatro réplicas e o Service expõe a aplicação na porta 5000.

**Conhecimentos aplicados:** Kubernetes, manifests YAML, Deployments, Services, réplicas, labels, selectors e organização declarativa de recursos.

### `network/` — Redes e comunicação entre containers

Apresenta cenários de conectividade em diferentes contextos.

**`network/1_externa/`**

Aplicação Flask que realiza uma requisição HTTP para `https://randomuser.me/api` e retorna o JSON recebido.

- `Dockerfile`: instala Flask e Requests e configura a execução da aplicação.
- `app.py`: implementa a rota que consome o serviço externo.

**`network/2_host/`**

Aplicação Flask configurada para acessar o MySQL disponível no host por meio de `host.docker.internal`.

- `app.py`: implementa consulta a uma API externa e uma rota POST `/inserthost`, que busca um nome aleatório e tenta inseri-lo na tabela `users`.
- `Dockerfile`: configura as dependências da aplicação, incluindo as bibliotecas necessárias para integração com MySQL.

**`network/3_conn_containers/`**

Demonstra a comunicação entre uma aplicação Flask e um banco MySQL executados em containers distintos.

- `flask/`: contém o Dockerfile e a aplicação Flask, configurada para acessar o serviço MySQL pelo nome `mysqlapicontainer`.
- `mysql/`: contém o Dockerfile e o arquivo `schema.sql`, utilizado na inicialização do banco.

**Conhecimentos aplicados:** redes Docker, conectividade externa, comunicação entre host e container, resolução de nomes, comunicação entre containers e integração com banco de dados.

### `teste/` — Exercício com FastAPI

Contém uma aplicação simples desenvolvida com FastAPI.

- `main.py`: implementa as rotas `/` e `/nome/{nome}`, demonstrando o uso de parâmetros de caminho.
- `dockerfile`: configura o ambiente Python e instala FastAPI e Uvicorn.

**Conhecimentos aplicados:** criação de APIs, rotas HTTP, parâmetros de caminho, Dockerfile e execução de aplicações Python em containers.

### `volumes/` — Persistência de arquivos

Contém uma aplicação PHP executada sobre a imagem `php:8-apache`, utilizada para demonstrar a gravação e a persistência de arquivos.

- `Dockerfile`: configura a imagem PHP com Apache.
- `index.php`: apresenta um formulário HTML para envio de mensagens.
- `process.php`: recebe os dados enviados por POST, cria arquivos sequenciais no diretório `messages/` e redireciona para a página inicial.
- `messages/`: armazena os arquivos de mensagens gerados pelo exercício.

**Conhecimentos aplicados:** volumes, bind mounts, persistência de arquivos, formulários HTML, requisições POST e execução de PHP com Apache.

### `yaml/` — Leitura e manipulação de YAML

Apresenta um exercício de leitura de arquivos YAML com Python.

- `app.py`: utiliza `yaml.safe_load` para carregar o conteúdo do arquivo e percorrer os dados interpretados.
- `test.yaml`: apresenta estruturas de configuração com tipos escalares, listas e objetos.

**Conhecimentos aplicados:** YAML, leitura de arquivos de configuração, estruturas de dados e processamento de informações com Python.

## Principais implementações

### Construção e execução de imagens Docker

Os Dockerfiles do repositório demonstram as principais instruções utilizadas na construção de imagens:

| Instrução | Finalidade |
|---|---|
| `FROM` | Define a imagem base utilizada no ambiente. |
| `WORKDIR` | Configura o diretório de trabalho dentro do container. |
| `RUN` | Executa comandos durante a construção da imagem, como a instalação de dependências. |
| `COPY` | Copia arquivos do contexto de build para a imagem. |
| `EXPOSE` | Documenta a porta utilizada pela aplicação. |
| `CMD` | Define o comando padrão de inicialização do container. |

Os exemplos contemplam aplicações Node.js, Python, PHP e serviços MySQL.

### Desenvolvimento de APIs e aplicações web

O repositório utiliza diferentes frameworks para demonstrar a criação de aplicações HTTP:

- **Flask:** construção de aplicações web, renderização de templates, integração com APIs externas e comunicação com MySQL.
- **FastAPI:** criação de endpoints, respostas JSON e parâmetros de caminho.
- **Express:** desenvolvimento de rotas HTTP e APIs com respostas em texto e JSON.
- **PHP com Apache:** processamento de formulários e gravação de informações em arquivos.

### Integração e persistência com MySQL

Os exercícios de `network/` e `compose/` demonstram diferentes formas de conectar aplicações Flask a um banco MySQL.

Os cenários exploram:

1. Acesso ao banco disponível no host por meio de `host.docker.internal`.
2. Comunicação com um banco executado em outro container.
3. Comunicação utilizando nomes de serviços definidos no Docker Compose.

As aplicações Flask utilizam `flask_mysqldb` para estabelecer a conexão, executar comandos SQL, confirmar transações e fechar cursores. Os arquivos `schema.sql` definem o banco `flaskdocker` e a tabela `users`, com identificador autoincremental e coluna para armazenar nomes.

### Composição de aplicações com Docker Compose

Os arquivos `docker-compose.yaml` organizam serviços que precisam funcionar em conjunto. Os exemplos demonstram:

- Declaração de serviços e imagens.
- Construção de imagens a partir de Dockerfiles.
- Publicação de portas.
- Configuração de variáveis de ambiente.
- Criação de redes bridge.
- Definição de volumes nomeados.
- Compartilhamento de diretórios com bind mounts.
- Dependências entre serviços.

### Persistência com volumes e bind mounts

Os exercícios demonstram duas formas importantes de compartilhar e manter dados:

- **Volumes nomeados:** utilizados nos exemplos de MySQL para armazenar os dados do banco independentemente do ciclo de vida do container.
- **Bind mounts:** utilizados para compartilhar diretórios do host com o container, permitindo acessar arquivos diretamente pelo ambiente de execução.

A aplicação PHP em `volumes/` complementa o estudo ao gravar mensagens em arquivos no diretório `messages/`.

### Orquestração com Kubernetes

Os manifests YAML demonstram a definição declarativa de recursos Kubernetes.

- **Deployment:** descreve a aplicação e a quantidade desejada de réplicas.
- **Service:** disponibiliza um ponto de acesso para os pods.
- **Labels e selectors:** conectam os Services aos pods correspondentes.
- **Separação e união de manifests:** comparação entre recursos declarados em arquivos distintos e recursos agrupados em um único YAML.

### Integração com serviços externos

As aplicações Flask utilizam a biblioteca Requests para realizar chamadas HTTP à API pública `randomuser.me`. Os exemplos demonstram o consumo de dados externos e sua utilização em operações realizadas pela aplicação, incluindo a gravação de informações no MySQL.

## Conhecimentos técnicos aplicados

### Docker e conteinerização

Construção de imagens a partir de Dockerfiles, configuração de ambientes de execução, instalação de dependências, cópia de arquivos, exposição de portas e inicialização de aplicações em containers.

### Docker Compose

Organização de aplicações com múltiplos serviços, configuração de redes, volumes, variáveis de ambiente e dependências entre containers.

### Redes e comunicação

Configuração de comunicação entre containers, acesso do container ao host, resolução de nomes e consumo de serviços externos por meio de requisições HTTP.

### Volumes e persistência de dados

Utilização de volumes nomeados e bind mounts para manter dados e compartilhar arquivos entre o host e os containers.

### APIs e desenvolvimento web

Criação de rotas HTTP, endpoints, parâmetros de caminho e respostas em texto, HTML e JSON com Flask, FastAPI e Express.

### Banco de dados relacional

Integração de aplicações Python com MySQL, execução de comandos SQL, inserção de registros e utilização de scripts para criação de schemas e tabelas.

### Configuração declarativa

Utilização de arquivos YAML para descrever serviços Docker Compose e recursos Kubernetes, além da organização de parâmetros por meio de arquivos de ambiente.

### Kubernetes

Definição de Deployments e Services, configuração de réplicas, utilização de labels e selectors e organização de recursos por meio de manifests declarativos.

### Integração HTTP

Consumo de APIs externas com Python e Requests, tratamento dos dados retornados e utilização dessas informações em funcionalidades das aplicações.

## Como executar os exercícios

Os diretórios representam cenários independentes. Para executar um exercício, utilize os comandos a partir da raiz do repositório e selecione a pasta correspondente.

### Pré-requisitos

- Docker Engine ou Docker Desktop.
- Docker Compose v2 para os exercícios que utilizam arquivos Compose.
- Acesso à internet para baixar imagens e dependências e executar os exemplos que consomem serviços externos.
- Cluster Kubernetes e `kubectl` configurado para os exercícios de orquestração.

### Executar a aplicação FastAPI — `Projetos/0409/`

```bash
docker build -t conhecimento-docker-fastapi ./Projetos/0409
docker run --rm -p 8080:8080 conhecimento-docker-fastapi
```

A aplicação disponibiliza os endpoints `/` e `/lista_funcionarios` na porta 8080.

### Executar a aplicação Express — `Imagem/`

```bash
docker build -t conhecimento-docker-express ./Imagem
docker run --rm -p 3000:3000 conhecimento-docker-express
```

A aplicação disponibiliza as rotas `/` e `/hello-world` na porta 3000.

### Executar um exercício Docker Compose

Entre no diretório do cenário desejado e inicie os serviços:

```bash
cd compose/criacao_compose
docker compose up --build
```

Para encerrar os serviços:

```bash
docker compose down
```

O exemplo de WordPress publica a aplicação na porta 8000 do host. Os demais exercícios Compose devem ser iniciados a partir de seus respectivos diretórios.

### Executar a aplicação Flask — `network/1_externa/`

```bash
docker build -t conhecimento-docker-network ./network/1_externa
docker run --rm -p 5000:5000 conhecimento-docker-network
```

Esse exemplo utiliza Requests para consultar um serviço externo.

### Executar o exercício FastAPI — `teste/`

Como o arquivo Dockerfile está nomeado com letras minúsculas, indique seu caminho explicitamente:

```bash
docker build -f teste/dockerfile -t conhecimento-docker-teste ./teste
docker run --rm -p 8080:8080 conhecimento-docker-teste
```

### Aplicar manifests Kubernetes

Com um cluster configurado e acesso por meio do `kubectl`, aplique os manifests desejados:

```bash
kubectl apply -f kubernetes/2_modo_declarativo/flask.yaml
kubectl apply -f kubernetes/2_modo_declarativo/flask-service.yaml
```

Também é possível aplicar o cenário que reúne os recursos em um único arquivo:

```bash
kubectl apply -f kubernetes/3_uniao_arqs/flask-project.yaml
```

## Considerações finais

Este repositório reúne uma sequência de exercícios práticos voltados ao estudo de conteinerização e orquestração. Os exemplos permitem compreender como aplicações são empacotadas em imagens, executadas em containers, conectadas a bancos de dados e serviços externos, organizadas com Docker Compose e descritas por manifests Kubernetes.

A organização por cenários facilita a comparação entre diferentes abordagens e reforça conhecimentos sobre Docker, redes, persistência de dados, configuração de serviços e fundamentos de orquestração.
