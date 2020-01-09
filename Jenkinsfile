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
                        echo $PATH
                        . venv/bin/activate
                        echo $PATH
                        pip install -r requirements.txt
                       """
                }
            }
        }
        stage('Install secrender') {
            steps {
                script {
                    sh """
                        echo $PATH
                        . venv/bin/activate
                        echo $PATH
                        pip install -e .
                       """
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh """
                        echo $PATH
                        . venv/bin/activate
                        echo $PATH
                        secrender --help
                       """
                }
            }
        }       
    }
}
