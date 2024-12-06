pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
        DOCKERFILE_PATH = './app/Dockerfile'
        COMPOSE_FILE = './docker-compose.yml'
        PROMETHEUS_CONFIG = './monitoring/prometheus.yml'
        GRAFANA_DASHBOARD_PATH = './monitoring/grafana_dashboards'
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                script {
                    echo 'Clonando repositório...'
                    git url: 'https://github.com/marcodev1x/Trabalho_DevOps_23.9711-5.git', branch: 'main'
                }
            }
        }

        stage('Construir Imagem Docker') {
            steps {
                script {
                    echo 'Construindo imagem Docker...'
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} -f ${DOCKERFILE_PATH} ./app"
                }
            }
        }

        stage('Rodar Testes Unitários') {
            steps {
                script {
                    echo 'Executando testes unitários...'
                    sh "docker run --rm ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} pytest /app/test_app.py || exit 1"
                }
            }
        }

        stage('Deploy com Docker Compose') {
            steps {
                script {
                    echo 'Realizando deploy do ambiente com Docker Compose...'
                    sh "docker-compose -f ${COMPOSE_FILE} up -d"
                }
            }
        }

        stage('Configurar Monitoramento') {
            steps {
                script {
                    echo 'Configurando monitoramento com Prometheus e Grafana...'
                    // Validar configurações do Prometheus
                    sh "test -f ${PROMETHEUS_CONFIG}"
                    
                    // Verificar se as dashboards do Grafana estão presentes
                    sh "test -d ${GRAFANA_DASHBOARD_PATH}"
                    
                    echo 'Monitoramento configurado.'
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Pipeline executada com sucesso! Ambiente e monitoramento configurados.'
            }
        }
        failure {
            script {
                echo 'Pipeline falhou. Verifique os logs para identificar o problema.'
            }
        }
        always {
            script {
                echo 'Limpando ambiente...'
                sh "docker-compose -f ${COMPOSE_FILE} down || true"
                sh "docker rmi ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} || true"
            }
        }
    }
}
