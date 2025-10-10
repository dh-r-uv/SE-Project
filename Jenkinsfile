pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'dhruvk321'
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/calculator-app"
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS_ID = 'docker-credentials'
        EMAIL = 'dhruvkothari4017@gmail.com'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 -m unittest discover'
                echo 'Unit tests passed.'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '.')
                }
            }
        }


        stage('Push to Docker Hub') {
            steps {
                // Logs into Docker Hub and pushes the image 
                script {
                     withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                        sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
                        sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                        sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
                        sh "docker push ${IMAGE_NAME}:latest"
                    }
                }
                echo "Pushed Docker image to Docker Hub."
            }
        }

        stage('Deploy via Ansible') {
            steps {
                withEnv(["BUILD_NUMBER=${BUILD_NUMBER}"]) {
                    sh '''
                    ansible-playbook -i inventory.ini deploy.yml
                    '''
                }
            }
        }
    }
    
    post {
        success {
            mail to: EMAIL,
                 subject: "SUCCESS: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                 body: "The pipeline run was successful. Check the build log here: ${env.BUILD_URL}"
        }
        failure {
            mail to: EMAIL,
                 subject: "FAILURE: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                 body: "The pipeline run failed. Check the build log for errors: ${env.BUILD_URL}"
        }
    }
}