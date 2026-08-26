pipeline {
    agent any

    stages {

        stage('Check Environment') {
            steps {
                sh 'docker --version'
                sh 'python3 --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t automated-devops-app .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                sh 'docker stop automated-devops-container || true'
                sh 'docker rm automated-devops-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name automated-devops-container -p 5000:5000 automated-devops-app'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000/health'
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
