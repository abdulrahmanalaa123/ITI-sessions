FROM ubuntu:plucky-20241213
RUN apt update && apt install ssh sudo -y
RUN adduser iti
RUN echo "iti:123" | chpasswd
RUN gpasswd -a iti sudo
ENTRYPOINT service ssh start && bash 
