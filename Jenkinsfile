pipeline {
    agent any
    stages {
        stage('BuildImage') {
            steps {
                script{
                    echo 'building the application'
                    //sh 'docker rmi myapp'
                    sh 'docker build -t pythonapp .'
                }
            }
        }
        stage('deployment') {
            steps {
                script{
                    echo 'deploying the app'
                    sh 'docker run -ti -d pythonapp'
                }
            }
        }
        stage('Deliver') {
            steps {
                script{
                   echo 'Deliver stage deploy on some server'
                }
            }
        }
     }
     }
