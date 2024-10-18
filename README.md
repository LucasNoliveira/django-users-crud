# Teste técnico - GoAndSlay

## Primeira Parte
Esta parte do projeto é uma API para gerenciamento de usuários, desenvolvida com Django e Django Rest Framework. A API permite criar, atualizar, deletar e recuperar usuários com autenticação JWT. O projeto foi configurado para ser executado em um ambiente Docker.

### Sumário

- [Pré-requisitos](#pré-requisitos)
- [Configuração do Projeto](#configuração-do-projeto)
  - [1. Clonar o Repositório](#1-clonar-o-repositório)
  - [2. Configurar Variáveis de Ambiente](#2-configurar-variáveis-de-ambiente)
  - [3. Executar o Projeto com Docker](#3-executar-o-projeto-com-docker)
  - [4. Acessar a API](#4-acessar-a-api)
- [Endpoints da API](#endpoints-da-api)
  - [Autenticação](#autenticação)
  - [Gerenciamento de Usuários](#gerenciamento-de-usuários)
- [Considerações Finais](#considerações-finais)

---

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados:

- **Docker**: Para gerenciar containers
- **Docker Compose**: Para gerenciar múltiplos containers
- **Git**: Para clonar o repositório

### Configuração do Projeto

#### 1. Clonar o Repositório

Primeiro, clone o repositório do projeto:

```bash
git clone https://github.com/LucasNoliveira/django-users-crud.git
cd django-users-crud
```

#### 2. Configurar Variáveis de Ambiente
   Renomeie o arquivo .env.example para .env e inclua as variáveis:

##### Exemplo:
```
DB_NAME=users_crud
DB_USER=postgres
DB_PASSWORD=root

DEBUG=True
ALLOWED_HOSTS=localhost

```
Ajuste as variáveis conforme necessário para o seu ambiente de desenvolvimento.

#### 3. Executar o Projeto com Docker
Para rodar o projeto em um container Docker, execute o seguinte comando na raiz do projeto (onde o Dockerfile está localizado):
```
docker compose up --build
```

Este comando irá:

* Construir a imagem Docker com base no Dockerfile
* Instalar as dependências com base no arquivo requirements.txt
* Executar as migrações para o banco de dados PostgreSQL, criando o banco de dados e suas tabelas
* Rodar o container expondo a API na porta 8000

#### 4. Acessar a API
```
https://localhost:8000/api/v1/
```
Os principais endpoints estão documentados na seção a seguir.

### Endpoints da API
#### Autenticação
* Login:
  ##### Exemplo de Request:
 ``` {
  "email": "user@example.com",
  "password": "sua-senha"
}
```

  Envia as credenciais (email e senha) para obter um token JWT que PRECISARÁ ser enviado nas headers dos endpoints de gerenciamento de usuários.

 ###### Exemplo de Response:
```{
  "refresh": "token_refresh",
  "access": "token_access"
}
```

#### Gerenciamento de Usuários
Para acessar os endpoints a seguir é necessário enviar o token no cabeçalho da requisição 

* Criar usuário (não precisa de JWT): POST /users/
Cria um novo usuário.

* Listar Usuários (não precisa de JWT): GET /users/
Retorna uma lista de todos os usuários.

* Detalhes de Usuário (não precisa de JWT): GET /users/{id}/
Retorna os detalhes de um usuário específico.

* Atualizar Usuário: PUT /users/{id}/
Atualiza os dados de um usuário (somente o próprio usuário pode ser atualizado).

* Deletar Usuário: DELETE /users/{id}/
Remove um usuário (somente o próprio usuário pode ser deletado).

## Segunda Parte - Manipulação de HTML Armazenado no Banco
Este projeto é uma API para armazenar e gerenciar lições com conteúdo HTML, desenvolvida com Django e Django Rest Framework. Ele permite a criação, edição, exclusão e listagem de lições, com foco na manipulação de conteúdo HTML dentro do banco de dados. Não é necessário autenticação.

### Pré-requisitos

Os requisitos são os mesmo pois o módulo de lições é um Django app do projeto.

#### Acessar a API
```
http://localhost:8000/api/v1/
```

### Endpoints da API
* Criar Lição: POST /licoes/criar/
Cria uma nova lição com título e conteúdo HTML.
##### Exemplo de Request:
```
{
  "titulo": "Lição 1",
  "conteudo_html": "<h1>Bem-vindo à Lição</h1><p>Esta é uma lição de exemplo</p>"
}

```
##### Exemplo de Response:
```
{
  "id": 1,
  "titulo": "Lição 1",
  "conteudo_html": "<h1>Bem-vindo à Lição</h1><p>Esta é uma lição de exemplo</p>"
}

```

* Listar Lições: GET /licoes/
Retorna uma lista de todas as lições cadastradas no banco de dados.

##### Exemplo de Response:
```
[
  {
    "id": 1,
    "titulo": "Lição 1",
    "conteudo_html": "<h1>Bem-vindo à Lição</h1><p>Esta é uma lição de exemplo</p>"
  },
  {
    "id": 2,
    "titulo": "Lição 2",
    "conteudo_html": "<h1>Lição 2</h1>"
  }
]

```

* Editar Conteúdo HTML: PUT /licoes/{id}/editar-html/
Modifica o conteúdo HTML de uma lição existente. Este endpoint pode ser usado para alterar o estilo ou adicionar funções JavaScript ao conteúdo HTML.

##### Exemplo de Request:
```
{
  "conteudo_html": "<button style='color: red;'>Clique aqui</button><script>alert('Botão clicado!');</script>"
}

```

##### Exemplo de Response:
```
{
  "message": "Conteúdo HTML atualizado com sucesso"
}

```

* Deletar Lição: DELETE /licoes/{id}/deletar/
Remove uma lição do banco de dados.
##### Exemplo de Response:
```
{
  "message": "Lição deletada com sucesso"
}
```

### Considerações Finais
Este projeto foi configurado para fornecer uma API simples de gerenciamento de usuários e também criação e manipulação de HTML no banco de dados. Com o uso de Docker, o ambiente é facilmente replicável em qualquer máquina.


