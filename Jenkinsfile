pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
    }

    stages {
        stage('Preparação') {
            steps {
                script {
                    git url: 'https://github.com/marcodev1x/Trabalho_DevOps_23.9711-5.git', branch: 'main'
                }
            }
        }

        stage('Instalação de Dependências') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    sh 'docker-compose run --rm web pytest app/test_app.py'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    sh 'docker-compose up -d' // Sobe os containers em segundo plano
                }
            }
        }

        stage('Monitoramento com Prometheus e Grafana') {
            steps {
                script {
                    echo "Monitoramento configurado no Prometheus e Grafana"
                }
            }
        }
    }

    post {
        always {
            // Limpeza, se necessário
            cleanWs()
        }

        success {
            echo 'Pipeline executada com sucesso!'
        }

        failure {
            echo 'Pipeline falhou!'
        }
    }
}
