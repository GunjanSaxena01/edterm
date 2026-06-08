pipeline{
    agent any
    stages{
        stage('clone'){
            steps{
                checkout scm
        }
    }
    stage('Build'){
        steps{
            sh 'docker build -t flask-demo .'
        }
    }
    stage('Deploy'){ 
        steps{
            sh 'docker service update --image flask-demo webapp || docker service create --name webapp -p 5000:5000 flask-demo'
        }
    }
    }

}