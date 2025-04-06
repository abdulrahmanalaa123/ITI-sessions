
FROM jenkins/jenkins:lts

ARG CURR_USER="1000"
ARG DOCKER_GID="999"
ENV JENKINS_USER=jenkins CASC_JENKINS_CONFIG=/var/jenkins_home/config.yaml

USER root

RUN apt-get update &&\
	apt-get install ca-certificates curl &&\
	install -m 0755 -d /etc/apt/keyrings &&\
	curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && chmod a+r /etc/apt/keyrings/docker.asc

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
  apt-get update

RUN apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

ADD --chmod=744 plugins.txt  /provisioning/

ADD config.yml /var/jenkins_home/

# JAVA_OPTS is done to disable the setup wizard on first installation
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/config.yml JAVA_OPTS=-Djenkins.install.runSetupWizard=false


RUN userdel jenkins && adduser -u ${CURR_USER} ${JENKINS_USER}

RUN groupadd -for -g ${DOCKER_GID} docker &&\
    usermod -aG docker ${JENKINS_USER}

# cant make the user variable depending on the JENKINS_USER  so leave it as jenkins
USER jenkins

RUN /bin/jenkins-plugin-cli --plugin-file /provisioning/plugins.txt

