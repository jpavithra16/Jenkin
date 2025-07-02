pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install Python (Optional)') {
            steps {
                echo 'Assuming Python is already installed on the Windows agent.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests using Python'
                bat 'python -m unittest test_calculator.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo '✅ All tests passed.'
        }
        failure {
            echo '❌ Some tests failed.'
        }
    }
}
