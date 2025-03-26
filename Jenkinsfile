pipeline{
    agent any

    stages{
        stage ("Checkout code"){
            steps{
                git credentialId : 'Pat_project' , url: 'https://github.com/Keerthana3838/New_repo.git' , branch:'main'
            }

        }
        stage ("Install deprndencies"){
            steps{
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                '''
            }
        }
        stage ("Run python code"){
            steps{
                bat '''
                call venv\\Scripts\\activate
                python sign_up.py
                '''

            }
        }
        stage ("Deploy"){
            steps{
                echo "Deploying applications"
            }
        }
            
        
    }
    post {
        success{
            echo "pipeline succeed"
        }
        failure{
            echo "pipeline failures"
        }
    }
}