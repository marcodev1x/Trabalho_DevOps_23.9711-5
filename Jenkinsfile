pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devops-final-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
        PROMETHEUS_PORT = '9090'
        GRAFANA_PORT = '3000'
        DB_PORT = '3307'
        NETWORK_NAME = 'pipeline_network'
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

        stage('Criar Rede Docker') {
            steps {
                script {
                    echo 'Criando rede Docker, se necessário...'
                    sh "docker network create ${NETWORK_NAME} || true"
                }
            }
        }

        stage('Limpar Containers Antigos') {
            steps {
                script {
                    echo 'Removendo containers antigos...'
                    sh 'docker-compose down --remove-orphans'
                }
            }
        }

        stage('Construir Imagens') {
            steps {
                script {
                    echo 'Construindo imagens Docker...'
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }

        stage('Rodar Testes Unitários') {
            steps {
                script {
                    echo 'Executando testes unitários...'
                    sh 'docker-compose run --rm web pytest test_app.py'
                }
            }
        }

        stage('Subir Aplicação') {
            steps {
                script {
                    echo 'Iniciando aplicação em containers...'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Configurar Prometheus e Grafana') {
            steps {
                script {
                    echo 'Iniciando Prometheus e Grafana...'
                    sh """
                    docker run -d --network ${NETWORK_NAME} \
                        --name prometheus \
                        -p ${PROMETHEUS_PORT}:9090 \
                        -v \$(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
                        prom/prometheus

                    docker run -d --network ${NETWORK_NAME} \
                        --name grafana \
                        -p ${GRAFANA_PORT}:3000 \
                        grafana/grafana
                    """
                }
            }
        }

        stage('Configurar Monitoramento') {
            steps {
                script {
                    echo """
                    Monitoramento configurado com Prometheus e Grafana.
                    - Prometheus: http://localhost:${PROMETHEUS_PORT}
                    - Grafana: http://localhost:${GRAFANA_PORT}
                    """
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
                echo 'Pipeline finalizada. Realizando limpeza adicional, se necessário.'
                sh 'docker-compose logs > pipeline_logs.txt || true'
            }
        }
    }
}
