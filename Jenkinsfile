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
                sh 'docker build --no-cache -t automated-devops-app:latest .'
            }
        }

        stage('Stop Old Application') {
            steps {
                sh 'docker rm -f automated-devops-container || true'
            }
        }

        stage('Deploy New Application') {
            steps {
                sh 'docker run -d --name automated-devops-container -p 5000:5000 automated-devops-app:latest'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'sleep 5'
                sh 'docker ps --filter "name=automated-devops-container"'
            }
        }
    }

    post {
        success {
            echo '======================================'
            echo 'DEPLOYMENT SUCCESSFUL!'
            echo 'New code is running on Docker.'
            echo '======================================'
        }

        failure {
            echo '======================================'
            echo 'DEPLOYMENT FAILED!'
            echo 'Check Jenkins console output.'
            echo '======================================'
        }
    }
}
