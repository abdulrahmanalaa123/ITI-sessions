# installing jenkins image with docker available inside the contianer

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
- clone the directory
```
git clone -n --depth=1 --filter=tree:0 https://github.com/abdulrahmanalaa123/ITI-sessions iti
cd iti
git sparse-checkout set --no-cone /jenkins
git checkout
```
- now simply build the docker image with defining a couple of arguments beforehand
```
export CURR_USER=$(id -u)
export DOCKER_GID=$(stat -c '%g' /var/run/docker.sock)
docker build --build-arg CURR_USER --build-arg DOCKER_GID -t jenkins_docker .
```

## Running the container

- if the container is in rootless mode or has userns enabled you can check using theses commands  [saviour](https://forums.docker.com/t/docker-sock-mount-permission/118720)
```
docker info | grep -i rootless
docker info | grep -i userns
```
- run the container with mounting the user socket to the container and simply replace the username and password with your desired admin user and password

```
docker run -it --name=jenkins --rm -p 8080:8080  -p 50000:50000 --env JENKINS_ADMIN_ID=username --env JENKINS_ADMIN_PASSWORD=password --env JENKINS_LOCATION=http://localhost:8080 -v jenkins:/var/jenkins_home -v /var/run/user/"$(id -u)"/docker.sock:/var/run/docker.sock jenkins_docker
```
- if you dont have docker rootless or userns enabled run the following command [good but incomplete reference](https://blog.nestybox.com/2019/09/29/jenkins.html)
```
docker run -it --name=jenkins --rm -p 8080:8080  -p 50000:50000 --env JENKINS_ADMIN_ID=username --env JENKINS_ADMIN_PASSWORD=password --env JENKINS_LOCATION=http://localhost:8080 -v jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins_docker
```

## Notes
- There was an issue of the volume created was taking the ownership of root after calling the jenkins docker image although not editing the file ownership so had to change the ownership of referenced files following the [jenkins official dockerfile](https://github.com/jenkinsci/docker/blob/587b2856cd225bb152c4abeeaaa24934c75aa460/Dockerfile)
- and changing the jenkins id for the current user and changing all the files' permissions to the new id in the dockerfile following [this](https://askubuntu.com/questions/16700/how-can-i-change-my-own-user-id)
- editing the run command after discovering a note in [the jenkins docker docs](https://github.com/jenkinsci/docker?tab=readme-ov-file#usage) although it can be solved by adding the -u as -u root but idk the implications of such a thing
```
NOTE: Avoid using a bind mount from a folder on the host machine into /var/jenkins_home, as this might result in file permission issues (the user used inside the container might not have rights to the folder on the host machine). If you really need to bind mount jenkins_home, ensure that the directory on the host is accessible by the jenkins user inside the container (jenkins user - uid 1000) or use -u some_other_user parameter with docker run.
```
