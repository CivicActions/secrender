pipeline {
    agent {
        docker {
            image 'python:3.7.5'
        }
    }
    stages {
        stage('Install dependencies') {
            steps {
                script {
                    sh """
                        python -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                       """
                }
            }
        }
    }
}
