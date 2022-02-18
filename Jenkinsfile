pipeline {
    agent { label 'master' }
    stages {
        stage('SCM') {
            steps {
                //git branch: 'main', poll: false, url: 'https://github.com/AnandhuCC/python-test-reconstruction.git'
                git branch: 'main', poll: false, url: 'https://github.com/AnandhuCC/python-test-filtering.git'
            }
        }
        stage('SonarQube analysis') {
            steps {
                //def scannerHome = tool 'SonarScanner 4.0';
                
                withSonarQubeEnv('sonarQube1') {
                    
                    //gradle
                    /*
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=python-test \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://localhost:9000 \
                          -Dsonar.login=2ce128543b463ac5f2ebfabde248d837c38f5442
                    '''
                    */
                    //sh "${scannerHome}/bin/sonar-scanner"
                    sh "${tool("sonar")}/bin/sonar-scanner;printenv"
                    
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
