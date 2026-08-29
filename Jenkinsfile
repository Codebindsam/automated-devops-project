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

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image..."
                    docker build --no-cache -t automated-devops-app:latest .
                    docker images | grep automated-devops-app
                '''
            }
        }

        stage('Prepare Container') {
            steps {
                sh '''
                    echo "Removing old container if it exists..."
                    docker rm -f automated-devops-container 2>/dev/null || true
                '''
            }
        }

        stage('Terraform Init') {
            steps {
                sh '''
                    terraform -chdir=terraform init
                '''
            }
        }

        stage('Terraform Apply') {
            steps {
                sh '''
                    terraform -chdir=terraform apply -auto-approve
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Waiting for application..."
                    sleep 5

                    echo "Checking container..."
                    docker ps --filter "name=automated-devops-container"

                    echo "Checking application health..."
                    curl -f http://localhost:5001/health
                '''
            }
        }
    }

    post {
        success {
            echo '''
            ========================================
                  CI/CD PIPELINE SUCCESSFUL
            ========================================
            '''
        }

        failure {
            echo '''
            ========================================
                  CI/CD PIPELINE FAILED
            ========================================
            '''
        }
    }
}
