pipeline{
agent {node {label 'workers'}}
 	stages{
		stage('create html file'){
			steps{
				sh '''
					if [[ ! -e 00_marathon/index.db ]];then
						python3 00_marathon/create_db.py
					fi

					python3 00_marathon/gen_html.py

				   '''
			}
		}
		stage ('create docker with new index.html'){
			steps{
				sh '''
					docker build -t html_app:latest -f 00_marathon/Dockerfile .
				   '''
			}
		}
		stage('deploying docker container with  new app'){
			steps{
			sh '''
				docker run -d -p 80:8080 --name=html_$(date +%Y) html_app
			   '''
			}

		}

		stage('testing docker container with curl'){

			steps{
				sh '''
					container_ip=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' html_$(date +%Y))

					if $(which curl);then
						curl $container_ip
					else
						sudo yum install -y  curl
						
						curl $container_ip
					fi
					
				'''
			}
		
		}
		stage('Remove Docker Containers') {
			steps{
          			sh '''
					docker container stop $(docker ps --all --quiet)					
				'''
			}
        	}
	 }
	
	post{
		always{
			cleanWs(cleanWhenSuccess: true, 
			deleteDirs: true, 
			externalDelete: 'docker container rm html_2021',
			notFailBuild: true)
			}
	}
}
