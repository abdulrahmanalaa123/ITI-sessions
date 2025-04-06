# installing jenkins image with docker available inside the contianer

## Requirements
- you need to install docker first
```
curl -fsSL https://get.docker.com -o install-docker.sh
sudo sh install-docker.sh
```
- and add the user to the docker group
```
sudo groupadd docker
sudo gpasswd -a $USER docker
```
- either relogin or run in newgrp docker
```
newgrp docker
```

## installation
- the plugins file is exported from the jenkins default plugins installed in a freshly setup jenkins image
```
JENKINS_HOST=username:password@localhost:8080
curl -sSL "http://$JENKINS_HOST/pluginManager/api/xml?depth=1&xpath=/*/*/shortName|/*/*/version&wrapper=plugins" | perl -pe 's/.*?<shortName>([\w-]+).*?<version>([^<]+)()(<\/\w+>)+/\1 \2\n/g'|sed 's/ /:/' > plugins.txt
```
- and adding the casc plugin as well as the authorization plugin with roles
```
authorize-project:latest
configuration-as-code:latest
role-strategy:latest
```
- and for the config.yml a default yml was used from the [docker jenkins repo](https://github.com/trion-development/docker-jenkins-docker-client)
- now simply build the docker image with defining a couple of arguments beforehand
```
export CURR_USER=$(id -u)
export DOCKER_GID=$(stat -c '%g' /var/run/docker.sock)
docker build --build-arg CURR_USER --build-arg DOCKER_GID -t jenkins_docker .
```

## Running the container
- run the container with your defined user and password and configuring the port
```
docker run -it --name=jenkins --rm -p 8080:8080 --env JENKINS_ADMIN_ID=username --env JENKINS_ADMIN_PASSWORD=password --env JENKINS_LOCATION=http://localhost:8080 -v $HOME/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins_docker
```
