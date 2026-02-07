pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Yuvraj-Dixit6265/devops-incident-intelligence-platform.git'
            }
        }

        stage('Security Scan - Secrets') {
            steps {
                sh 'python devsecops/secret_scan.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-incident-intelligence:ci .'
            }
        }

        stage('Run Platform') {
            steps {
                sh 'docker run --rm devops-incident-intelligence:ci'
            }
        }
    }
}
