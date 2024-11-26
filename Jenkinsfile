pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
        PROMETHEUS_PORT = '9090'
        GRAFANA_PORT = '3000'
        DB_PORT = '3307'
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                script {
                    git url: 'https://github.com/marcodev1x/Trabalho_DevOps_23.9711-5.git', branch: 'main'
                }
            }
        }

        stage('Limpar Containers Antigos') {
            steps {
                script {
                    sh 'docker-compose down --remove-orphans'
                }
            }
        }

        stage('Construir Imagens') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }

        stage('Rodar Testes Unitários') {
            steps {
                script {
                    sh 'docker-compose run --rm web pytest test_app.py'
                }
            }
        }

        stage('Subir Aplicação') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Configurar Prometheus e Grafana') {
            steps {
                script {
                    sh """
                    docker network create pipeline_network || true
                    docker run -d --network pipeline_network --name prometheus -p ${PROMETHEUS_PORT}:9090 prom/prometheus --config.file=/etc/prometheus/prometheus.yml
                    docker run -d --network pipeline_network --name grafana -p ${GRAFANA_PORT}:3000 grafana/grafana
                    """
                }
            }
        }

        stage('Configurar Monitoramento') {
            steps {
                script {
                    echo 'Monitoramento configurado com Prometheus e Grafana'
                    echo 'Prometheus está acessível na porta 9090 e Grafana na porta 3000'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }

        failure {
            echo 'Pipeline falhou!'
        }
    }
}
