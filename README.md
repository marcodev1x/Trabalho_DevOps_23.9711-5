# Trabalho DevOps - Criação de Ambiente Monitorado com Pipeline CI/CD

## Objetivo

Este projeto tem como objetivo implementar e configurar um ambiente completo de aplicação web com monitoramento e pipeline CI/CD, utilizando as seguintes ferramentas:

- **Jenkins** para automação do pipeline.
- **Prometheus** e **Grafana** para monitoramento e visualização de métricas.
- **Flask** para aplicação web.

---

## Pré-requisitos

- Docker
- Docker Compose

---

## Configuração e Execução

### 1. Subir o Ambiente

1.  Navegue até a pasta raiz do projeto (onde está o arquivo `docker-compose.yml`).
2.  Execute o comando abaixo para construir as imagens e subir os serviços:

    ```bash
    docker-compose up --build
    ```

3.  Testar os Serviços
    Aplicação Flask

        URL: http://localhost:5000

Banco de Dados MariaDB

    Host: localhost
    Porta: 3307 (configurada para evitar conflitos com a porta padrão. Pessoalmente tive problemas ao configurar na porta padrão.)
    Credenciais:
        Usuário: devops_user
        Senha: devops_password
        Banco de Dados: devops

4. Acessar a aplicação:

   A aplicação estará disponível em http://localhost:5000. Você pode usar um navegador ou um cliente HTTP (como Postman) para acessar as rotas.
   GET /alunos: Retorna a lista de alunos.
   POST /alunos: Cria um novo aluno.

5. Teste automatizado

   Um teste automatizado irá acontecer sempre que a aplicação for ao ar, utilizando um usuário com RA aleatório como descrito no arquivo /app/test_app.py.
   Um log foi adicionado ao console quando este teste acontecer. É possível visualizar este novo usuário na rota GET /alunos.
