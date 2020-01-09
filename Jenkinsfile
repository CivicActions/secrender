pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                script {
                    sh """
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                       """
                }
            }
        }
    }
}
