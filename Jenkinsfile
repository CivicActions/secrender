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
        stage('Install secrender') {
            steps {
                script {
                    sh """
                        . venv/bin/activate
                        pip install -e .
                       """
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh """
                        . venv/bin/activate
                        pip list
                        pip freeze
                        echo $PATH
                        secrender --help
                       """
                }
            }
        }       
    }
}
