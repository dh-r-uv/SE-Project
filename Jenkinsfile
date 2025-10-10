pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'dhruvk321'
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/calculator-app"
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS_ID = 'docker-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                // Runs the PyUnit tests to validate the code 
                sh 'python3 -m unittest discover'
                echo 'Unit tests passed.'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the workspace
                    // Make sure Docker Pipeline plugin is installed
                    // docker.build("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}", '.')

                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '.')

                    // Optionally, you can push it to Docker Hub
                    // docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials-id') {
                    //     dockerImage.push()
                    // }

                    // echo "Docker image built: ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                }
            }
        }


        stage('Push to Docker Hub') {
            steps {
                // Logs into Docker Hub and pushes the image 
                script {
                    // docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS_ID) {
                    //     // docker.image("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                    //     // docker.image("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push("latest")
                    //     // sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    //     // sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
                    //     // sh "docker push ${IMAGE_NAME}:latest"
                    //     sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
                    //     sh "docker tag ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
                    //     sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
                    // }
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
        always {
            // Clean up old Docker images to save space
            sh "docker image prune -f"
            echo 'Pipeline finished.'
        }
    }
}