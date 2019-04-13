# Reference
# https://docs.docker.com/engine/examples/running_ssh_service/

# FROM centos:latest
FROM ubuntu:16.04

# RUN yum update -y && yum install -y openssh-server
RUN apt-get update && apt-get install -y openssh-server

# install python packages
# https://github.com/ansible/ansible/issues/46980
RUN apt-get install -y python-minimal python-simplejson

RUN mkdir /var/run/sshd
RUN echo 'root:Password123' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]