pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
        DOCKERFILE_PATH = './app/Dockerfile'
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
                    sh "docker run --rm ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} pytest test_app.py || exit 1"
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Pipeline executada com sucesso! Todos os testes passaram.'
            }
        }
        failure {
            script {
                echo 'Pipeline falhou. Verifique os logs para identificar o problema.'
            }
        }
        always {
            script {
                echo 'Pipeline finalizada. Removendo imagens Docker...'
                sh "docker rmi ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} || true"
            }
        }
    }
}
