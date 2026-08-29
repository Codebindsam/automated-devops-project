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
                    echo "Building latest Docker image..."
                    docker build --no-cache -t automated-devops-app:latest .
                    docker images | grep automated-devops-app
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

                    echo "Testing application..."
                    curl -f http://localhost:5001

                    echo ""
                    echo "Deployment successful!"
                '''
            }
        }
    }

    post {
        success {
            echo '========================================'
            echo ' CI/CD PIPELINE COMPLETED SUCCESSFULLY '
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo '       CI/CD PIPELINE FAILED            '
            echo '========================================'
        }
    }
}
