pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Yuvraj-Dixit6265/devops-incident-intelligence-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-incident-intelligence:ci .'
            }
        }

        stage('Run Incident Intelligence Platform') {
            steps {
                sh 'docker run --rm devops-incident-intelligence:ci'
            }
        }
    }
}
