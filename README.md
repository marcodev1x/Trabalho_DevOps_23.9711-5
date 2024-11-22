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
