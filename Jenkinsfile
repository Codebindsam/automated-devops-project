pipeline {
    agent any

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

        stage('Terraform Infrastructure') {
            steps {
                sh 'terraform -chdir=terraform init'
                sh 'terraform -chdir=terraform apply -auto-approve'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build --no-cache -t automated-devops-app:latest .'
            }
        }

        stage('Stop Old Application') {
            steps {
                sh 'docker stop automated-devops-container || true'
                sh 'docker rm automated-devops-container || true'
            }
        }

        stage('Deploy New Application') {
            steps {
                sh '''
                    docker run -d \
                      --name automated-devops-container \
                      --network automated-devops-network \
                      -p 5000:5000 \
                      automated-devops-app:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}
