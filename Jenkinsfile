pipeline {
    agent any
    stages {
        stage('CleanUp Stage') {
            steps {
                echo "Cleanup"
                //cleanWs()
            }
        }
        stage('CheckOut Stage') {
            steps {
                echo "Updates files in  the working tree to match the version in the index or sprecified tree."
                checkout scm
            }
        }
        stage('Build Stage') {
            steps {
                sh 'sudo su'
                sh 'sudo yum update -y'
                echo "Create and enter virtual environment"
                sh 'sudo yum install python-virtualenv'
        		sh 'virtualenv myvirtualenv'
                sh 'source myvirtualenv/bin/activate'
                echo "Installing python and other essentials."
                sh 'sudo yum install python3'
                echo "Do unit test."
                sh 'python3 -m CalcTest.test'
            }
        }        
    }
}
