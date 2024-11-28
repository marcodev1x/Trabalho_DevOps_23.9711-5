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

        stage('Criar Rede Docker') {
            steps {
                script {
                    echo 'Criando rede Docker, se necessário...'
                    sh """
                    if ! docker network inspect ${NETWORK_NAME} > /dev/null 2>&1; then
                        docker network create ${NETWORK_NAME}
                    fi
                    """
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

        stage('Subir Aplicação') {
            steps {
                script {
                    echo 'Iniciando aplicação em containers...'
                    sh "docker-compose -f ${COMPOSE_FILE} up -d"
                }
            }
        }

        stage('Configurar Prometheus e Grafana') {
            steps {
                script {
                    echo 'Iniciando Prometheus e Grafana...'
                    sh """
                    # Remove containers antigos, se existirem
                    docker rm -f prometheus || true
                    docker rm -f grafana || true
                    
                    # Inicia o Prometheus
                  docker run -d --network ${NETWORK_NAME} \
                  --name prometheus \
                  --init \
                  -p ${PROMETHEUS_PORT}:9090 \
                  -v ${WORKSPACE}/prometheus.yml:/etc/prometheus/prometheus.yml \
                   prom/prometheus || true

                   docker run -d --network ${NETWORK_NAME} \
                   --name grafana \
                   --init \
                   -p ${GRAFANA_PORT}:3000 \
                    grafana/grafana || true

                    """
                }
            }
        }

        stage('Verificar Configuração de Monitoramento') {
            steps {
                script {
                    echo "Monitoramento configurado com sucesso:"
                    echo " - Prometheus: http://localhost:${PROMETHEUS_PORT}"
                    echo " - Grafana: http://localhost:${GRAFANA_PORT}"
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
