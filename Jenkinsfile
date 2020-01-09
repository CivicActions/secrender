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
                        python -m venv /tmp/venv
                        echo $PATH
                        . /tmp/venv/bin/activate
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
                        env
                        . /tmp/venv/bin/activate
                        env
                        pip install -e .
                       """
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh """
                        env
                        . /tmp/venv/bin/activate
                        env
                        secrender --help
                       """
                }
            }
        }       
    }
}
