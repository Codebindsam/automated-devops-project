pipeline {
    agent any

    stages {

        stage('Check Environment') {
            steps {
                sh 'docker --version'
                sh 'python3 --version'
                sh 'terraform --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t automated-devops-app .'
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform -chdir=terraform init'
            }
        }

        stage('Terraform Apply') {
            steps {
                sh 'terraform -chdir=terraform apply -auto-approve'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:5001/health'
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
