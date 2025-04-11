

FROM jenkins/jenkins:lts

#DOCKER_GID cant take the 999 id because systemd-journal takes it
ARG DOCKER_GID="999"
ARG CURR_USER="1000"

ADD --chmod=744 plugins.txt config.yml /provisioning/

ENV JENKINS_USER=jenkins
ENV CASC_JENKINS_CONFIG=/provisioning
ENV PLUGINS=/provisioning/plugins.txt
ENV JENKINS_HOME=/var/jenkins_home

# JAVA_OPTS is done to disable the setup wizard on first installation
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false

USER root

RUN apt-get update &&\
	apt-get install ca-certificates curl &&\
	install -m 0755 -d /etc/apt/keyrings &&\
	curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && chmod a+r /etc/apt/keyrings/docker.asc

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
  apt-get update

RUN apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# adding the group docker inside the container with the same user id and the group id outside the container to have the same permissions for accessing the docker socket
RUN groupadd -for -g $DOCKER_GID named_group
# adding the group using the id in case docker was given a different id 
RUN usermod -aG $DOCKER_GID $JENKINS_USER 

# change the ownership to the jenkins user
RUN chown -R $JENKINS_USER:jenkins $JENKINS_HOME 
RUN chown -R $JENKINS_USER:jenkins /usr/share/jenkins/ref

# changing the ownership first in root before changing to be able to find the old_Id without env vars (only useful in case the current user_id isnt the default 1000) which is the default for jenkins
RUN export old_id=$(id -u "$JENKINS_USER") && find / -xdev -uid "$old_id" -exec chown "$CURR_USER" '{}' \+ && \
    usermod -u "$CURR_USER" "$JENKINS_USER"

USER ${JENKINS_USER}

RUN /bin/jenkins-plugin-cli --plugin-file ${PLUGINS}

