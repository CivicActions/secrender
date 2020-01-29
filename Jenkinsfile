pipeline {
    agent {
        docker {
            image 'python:3.7.5'
        }
    }
    stages {
        stage('Install') {
            environment {
                POETRY_HOME = "poetry"
                HOME = "."
            }
            steps {
                script {
                    sh """
                        pwd
                        mkdir -p poetry poetry-cache
                        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
                        poetry/bin/poetry config cache-dir poetry-cache
                        poetry/bin/poetry config virtualenvs.in-project true
                        poetry/bin/poetry install
                       """
                }
            }
        }
        stage('Static Checks') {
            steps {
                script {
                    sh '''
                        poetry/bin/poetry run flake8 secrender
                       '''
                }
            }

        }
        stage('Unit Tests') {
            steps {
                script {
                    sh '''
                        poetry/bin/poetry run coverage run --source=secrender -m pytest -v tests
                        poetry/bin/poetry run coverage report -m
                        poetry/bin/poetry run coverage html
                       '''
                }
                archive includes: 'htmlcov'
            }
        }       
        stage('Functional Tests') {
            steps {
                script {
                    sh '''
                        cd examples
                        ../poetry/bin/poetry run secrender --in example.yaml --template example.md.j2 --output example.md
                        cat example.md
                        ../poetry/bin/poetry run secrender --in example-include.yaml --template example.md.j2 --output example.md
                        cat example.md
                      '''
                }
            }
        }
    }
}
