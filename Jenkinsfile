pipeline{
    agent any
    envriornment{
        "tanishk659/flask-demo"
    }
    stages{
        stage('Checkout){
            steps{
                checkout scm
            }
        }
        stage('Build'){
            steps {bat 'docker build -t %IMAGE_NAME% .}  
        }
        stage('Docker login'){
            steps{
                withCredentials([usernamePassword(credentailsId:'dockerhub-creds',usernameVariable:'DOCKER_USER',passwordVariable:'DOCKER_PASS')]){
                    bat ''' echo %DOCKER_PASS% |docker login -u %DOCKER_USER% --password-stdin'''
                }
            }
        }
        stage('deploy to swarm'){
            steps{
                bat ''' docker service update --image %IMAGE_NAME% webapp '''
            }
        }
    }

    post{
        success{
            echo 'pipeline executed'
        }
        failiure{
            echo 'pipleine failed'
        }
    }


}