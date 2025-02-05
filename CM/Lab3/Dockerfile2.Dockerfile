FROM centos
RUN sed -E -i 's/http:\/\/mirror(list)?/http:\/\/vault/g' /etc/yum.repos.d/*
RUN sed -E -i 's/^#baseurl=/baseurl=/g' /etc/yum.repos.d/*
RUN yum -y update && yum clean all
RUN yum install openssh-server openssh-clients -y
RUN yum install sudo -y
RUN /usr/bin/ssh-keygen -A
# dont know the consquences of such action
RUN rm /run/nologin
RUN adduser iti
RUN echo "iti:123" | chpasswd
RUN gpasswd -a iti wheel
ENTRYPOINT  /usr/sbin/sshd -DE /tmp/sshd.log 
