pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
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

        stage('Executar Testes') {
            steps {
                script {
                    sh 'docker-compose run --rm web pytest app/test_app.py'
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

        stage('Configurar Monitoramento') {
            steps {
                script {
                    echo 'Monitoramento configurado com Prometheus e Grafana'
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
