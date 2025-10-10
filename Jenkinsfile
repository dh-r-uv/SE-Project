pipeline {
    agent any

    environment {
        // IMPORTANT: Change 'your-dockerhub-username' to your actual Docker Hub username
        DOCKERHUB_USERNAME = 'dhruvk321'
        // IMPORTANT: Change 'scientific-calculator' to your desired image name
        IMAGE_NAME = "calculator-app"
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        // This references the credentials you must set up in Jenkins
        DOCKERHUB_CREDENTIALS_ID = 'docker-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // Fetches the code from your GitHub repository
                // git 'https://github.com/dh-r-uv/SE-Project.git'
                // echo 'Source code checked out successfully.'
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
                    docker.build("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}", '.')

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
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS_ID) {
                        // docker.image("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}").push()
                        // docker.image("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}").push("latest")
                        docker.image("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                        docker.image("${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push("latest")
                    }
                }
                echo "Pushed Docker image to Docker Hub."
            }
        }

        // stage('Deploy with Ansible') {
        //     steps {
        //         // Executes the Ansible playbook to deploy the container locally [cite: 17, 19]
        //         // We pass the image name as an extra variable to the playbook
        //         sh "ansible-playbook playbook.yml --extra-vars 'docker_image=${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest'"
        //         echo 'Deployment with Ansible complete.'
        //     }
        // }
    }
    
    post {
        always {
            // Clean up old Docker images to save space
            sh "docker image prune -f"
            echo 'Pipeline finished.'
        }
    }
}