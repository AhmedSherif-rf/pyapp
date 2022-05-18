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
                    sh 'docker run -it -d --name=app pythonapp'
                    sh 'sh script.sh'
                }
            }
        }
        stage('Deliver') {
            steps {
                script{
                   while (true) {
                     def cmd = input(message: 'Jenkins Interactive Shell', parameters: [
                     string(name: 'cmd', description: 'Enter a command or leave blank to continue job.', defaultValue: '')
                    ], ok: 'Execute')
                    if (cmd == '') { print 'Continuing job...'; break; }
                    try { sh cmd }
                    catch (err) { }
                    }
                }
            }
        }
     }
     }
