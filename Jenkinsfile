pipeline
{
    agent any

    stages {
        stage('Git checkout') {
            steps {
                git branch: 'es/jenkinsfile',
                    url: 'https://github.com/TA-user/RyanAir_Test_Automation.git'
            }
        }
	    stage('Prepare Selenoid') {
            steps {
                bat 'curl -L -o scm.exe https://github.com/aerokube/cm/releases/download/1.8.1/cm_windows_amd64.exe'
                bat 'move scm.exe etc\\selenoid\\scm.exe'
		        bat 'etc\\selenoid\\scm.exe selenoid start --vnc --args "-limit 4"'
		        bat 'etc\\selenoid\\scm.exe selenoid status'
		        bat 'etc\\selenoid\\scm.exe selenoid-ui start'
		        bat 'etc\\selenoid\\scm.exe selenoid-ui status'
		        bat 'curl http://localhost:4444/status'
            }
        }
	    stage('Running tests') {
            steps {
                bat 'pipenv install'
                bat 'pipenv shell'
                bat 'pipenv run pip list'
		        bat 'pipenv run python -m  pytest -n auto --username=%TEST_USER% --password=%TEST_PASSWORD% --browser_name=%BROWSER% --reruns 2 --alluredir=allure_reports'
            }
        }
    }

    post {
        always {
            script {
                bat 'docker stop selenoid'
                bat 'docker stop selenoid-ui'
                bat 'docker rm selenoid'
                bat 'docker rm selenoid-ui'
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_reports']]
                    ])
                archiveArtifacts artifacts:
                    'logs/debug.log, logs/errors.log',
                    followSymlinks: false
            }
        }
    }
}