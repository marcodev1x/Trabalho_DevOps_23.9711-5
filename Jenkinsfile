pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
        COMPOSE_FILE = 'docker-compose.yml'
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

        stage('Parar Containers Existentes') {
            steps {
                script {
                    echo 'Parando containers existentes...'
                    sh "docker-compose -f ${COMPOSE_FILE} down || true"
                }
            }
        }

        stage('Construir Imagens') {
            steps {
                script {
                    echo 'Construindo imagens Docker...'
                    sh "docker-compose -f ${COMPOSE_FILE} build"
                }
            }
        }

        stage('Rodar Testes Unitários') {
            steps {
                script {
                    echo 'Executando testes unitários...'
                    sh "docker-compose -f ${COMPOSE_FILE} run --rm web pytest test_app.py || exit 1"
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Pipeline executada com sucesso! Todos os passos foram concluídos.'
            }
        }
        failure {
            script {
                echo 'Pipeline falhou. Verifique os logs para identificar o problema.'
            }
        }
        always {
            script {
                echo 'Pipeline finalizada. Capturando logs...'
                sh "docker-compose -f ${COMPOSE_FILE} logs > pipeline_logs.txt || true"
                echo 'Logs salvos em pipeline_logs.txt'
            }
        }
    }
}
