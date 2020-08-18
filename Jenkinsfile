pipeline {
	agent any
	stages {
		stage ('CleanUp Stage') {
			steps {
				echo 'CleanUp of existing code and folder in jenkins'
				//cleanWs()
			}
		}
		stage('CheckOut Stage') {
			steps {
				echo 'Updates files in the working tree to match the version in the index or the specified tree.'
				checkout scm
			}
		}
		stage ('Build Stage') {
			steps {
				sh 'sudo su'
				sh 'sudo yum update'
				echo 'Creating a virtual environment'
				sh 'sudo yum install python-virtualenv'
				sh 'virtualenv myvirtualenv'
				sh 'source myvirtualenv/bin/activate'
				echo 'Installing python and other packages'
				sh 'sudo yum install python3'
				echo 'Running the unit test case file'
				sh 'python calculator_test.py'
			}
		}
		stage ('Deploy Stage') {
			steps {
				sh "sudo scp -i  '$WORKSPACE/20969-JD.pem' -o StrictHostKeyChecking=no -r calculator_main.py ec2-user@54.167.186.73:/home/ec2-user"
				sh "sudo scp -i  '$WORKSPACE/20969-JD.pem' -o StrictHostKeyChecking=no -r calculator_test.py ec2-user@54.167.186.73:/home/ec2-user"
				sh '''sudo ssh -i "20969-JD.pem" -o StrictHostKeyChecking=no ec2-user@ec2-user@54.167.186.73.compute-1.amazonaws.com 
				echo "Hello world" 
				sudo yum install python3
				sudo yum install python-virtualenv
				virtualenv env
				source env/bin/activate
				sudo pip3 install unittest2
				python3 calculator_test.py
				<<EOT'''
				echo 'Hello'
			}
		}
	}
}
