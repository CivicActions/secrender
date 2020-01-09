pipeline {
    agent {
        docker {
            image 'python:3.7.5'
        }
    }
    stages {
        stage('Install') {
            steps {
                script {
                    sh """
                        python -m venv /tmp/venv
                        . /tmp/venv/bin/activate
                        pip install -r requirements.txt
                        pip install -e .
                       """
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh """
                        . /tmp/venv/bin/activate
                        secrender --in examples/example.yaml --template examples/examples.md.j2
                        secrender --in examples/example-include.yaml --template examples/examples.md.j2
                       """
                }
            }
        }       
    }
}
