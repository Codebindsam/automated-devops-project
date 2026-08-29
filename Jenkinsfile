pipeline {
    agent any

    environment {
        IMAGE_NAME = 'automated-devops-app'
        CONTAINER_NAME = 'automated-devops-container'
        APP_PORT = '5000'
    }

    stages {

        stage('Checkout Latest Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                sh 'docker --version'
                sh 'python3 --version'
                sh 'terraform --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image from latest GitHub code..."

                    docker build --no-cache \
                        -t ${IMAGE_NAME}:build-${BUILD_NUMBER} \
                        -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Stop Old Application') {
            steps {
                sh '''
                    echo "Stopping old container..."

                    docker rm -f ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Deploy New Application') {
            steps {
                sh '''
                    echo "Starting new container..."

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${APP_PORT}:5000 \
                        ${IMAGE_NAME}:build-${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Waiting for application..."
                    sleep 5

                    echo "Checking application health..."
                    curl -f http://localhost:5000/health

                    echo ""
                    echo "Application deployed successfully!"
                '''
            }
        }
    }

    post {
        success {
            echo '======================================'
            echo 'DEPLOYMENT SUCCESSFUL'
            echo '======================================'
            echo "Application: http://localhost:5000"
            echo "Docker Image: ${IMAGE_NAME}:build-${BUILD_NUMBER}"
        }

        failure {
            echo '======================================'
            echo 'DEPLOYMENT FAILED'
            echo '======================================'
        }
    }
}
