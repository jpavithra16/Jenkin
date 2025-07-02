pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt || echo "No requirements.txt found"'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Some tests failed.'
        }
        success {
            echo 'All tests passed.'
        }
    }
}
