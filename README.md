# Trabalho DevOps - Criação de Ambiente Monitorado com Pipeline CI/CD

## Atenção!

Este trabalho foi feito com bastante carinho. Espero que atinja os requisitos necessários, obrigado pelas aulas, conhecimento entregue e também alguns momentos engraçados em aula. Abraço professor Wagner!

## Objetivo

Este projeto tem como objetivo implementar e configurar um ambiente completo de aplicação web com monitoramento e pipeline CI/CD, utilizando as seguintes ferramentas:

- **Jenkins** para automação do pipeline.
- **Prometheus** e **Grafana** para monitoramento e visualização de métricas.
- **Flask** para aplicação web.

---

## Pré-requisitos

- Python

- Docker

- Docker Compose

- Jenkins

---

## Configuração e Execução

### 1. Subir o Ambiente

1. Navegue até a pasta raiz do projeto (onde está o arquivo `docker-compose.yml`).
2. Execute o comando abaixo para construir as imagens e subir os serviços:

   ```bash
   docker-compose up --build
   ```

3. **Testar os Serviços**

   **Aplicação Flask**

   - URL: [`http://localhost:5000`](http://localhost:5000)

   **Banco de Dados MariaDB**

   - Host: `localhost`
   - Porta: `3307` (configurada para evitar conflitos com a porta padrão).
   - Credenciais:
     - **Usuário**: `devops_user`
     - **Senha**: `devops_password`
     - **Banco de Dados**: `devops`

4. **Acessar a aplicação**

   A aplicação estará disponível em [`http://localhost:5000`](http://localhost:5000).  
   Você pode usar um navegador ou um cliente HTTP (como Postman) para acessar as rotas:

   - **GET /alunos**: Retorna a lista de alunos.
   - **POST /alunos**: Cria um novo aluno.

5. **Teste automatizado & Jenkins**

   A aplicação Jenkins estará disponível em: http://localhost:8081

   - Um teste automatizado será executado sempre que a aplicação for inicializada, utilizando um usuário com RA aleatório, conforme descrito no arquivo `/app/test_app.py`.
   - Um log será exibido no console quando este teste ocorrer. É possível visualizar o novo usuário na rota **GET /alunos**.
   - Ao iniciar com o docker-compose up --build, uma senha parecida com essa "8bc1759450474428b296647b997b7626" será printada no console. Utilize ela para acessar o jenkins na rota específica.

---

## Monitoramento

O ambiente conta com monitoramento configurado via Prometheus e Grafana.

- **Prometheus**

  - URL: [`http://localhost:9090`](http://localhost:9090)

- **Grafana**
  - URL: [`http://localhost:3000`](http://localhost:3000)
  - Credenciais padrão:
    - **Usuário**: `admin`
    - **Senha**: `admin`
- Dentro do grafana, clique no botão "New database". Aqui, escolha a opção: "Prometheus" e a URL http://localhost:9090 (ou http://prometheus:9090 se tiver problemas em sua conexão por aí-).
- Após selecionar a database do Prometheus, selecione a opção de criar uma nova dashboard dentro do grafana. Preparei um arquivo aqui neste projeto .json que permitirá criar uma dashboard de maneira mais agilizada (./dashboard.json). Esse dashboard disponibilizará um leque de opções para visualizar as requisições flask e tempos de processamento. A dashboard e sua configuração fica a seu critério! Deixei um vídeo de uso aqui nesse projeto na pasta raiz.

Ao acessar o Grafana, você pode configurar o Prometheus como fonte de dados e importar dashboards personalizados para visualizar métricas detalhadas da aplicação.

Como Importar o Dashboard no Grafana

    Acesse o Grafana em http://localhost:3000.
    Faça login com o usuário e senha padrão (admin / admin).
    No menu lateral, clique em "+" e selecione Import.
    Clique em Upload .json file e selecione o arquivo dashboard.json que você deseja importar.
    Após o upload, selecione a fonte de dados (Prometheus) e clique em Import.

---

## CI/CD

O pipeline CI/CD foi configurado utilizando o Jenkins. Para configurar e rodar o Jenkins:

1. Acesse o Jenkins em [`http://localhost:8080`](http://localhost:8081).
2. Configure o pipeline utilizando o arquivo `Jenkinsfile` fornecido no repositório.
3. A cada alteração no repositório, o Jenkins irá:
   - Construir a aplicação.
   - Rodar testes automatizados.
   - Implantar a aplicação no ambiente configurado.
