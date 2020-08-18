pipeline {
    agent any
    stages {
        stage('clean') {
            steps {
                echo "Installing Python"
                sh 'sudo su'
                sh 'sudo yum install python3'
                echo "Create and enter virtual environment"
                sh 'sudo yum install python-virtualenv'
                sh 'virtualenv myvirtualenv'
                sh 'source myvirtualenv/bin/activate'
                echo ""
                sh 'python -m calc_test.test'
            }
        }
        stage('CheckOut Stage') {
            steps {
                echo "Updates files in  the working tree to match the version in the index or sprecified tree."
                checkout scm
            }
        }
        stage('build') {
            steps {
                echo "Installing Python"
                sh 'sudo su'
                sh 'sudo yum install python3'
                echo "Create and enter virtual environment"
                sh 'sudo yum install python-virtualenv'
            }
        }
        stage('unit test') {
        	steps {
        		echo "Perform unit test"
        		sh 'virtualenv myvirtualenv'
                sh 'source myvirtualenv/bin/activate'
                sh 'python3 -m calc_test.test'
        	}
        }
    }
}