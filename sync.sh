# rsync -avz --delete /Users/Eli/dev/devops/docker-centos root@192.168.1.110:/root/
# rsync -avz --delete /Users/Eli/dev/devops/docker-ubuntu root@192.168.1.110:/root/

ANSIBLE_CR="192.168.0.118"

cat ~/.ssh/id_rsa.pub | ssh "root@${ANSIBLE_CR}" "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
rsync -avz --delete /Users/Eli/dev/devops/docker-ubuntu "root@${ANSIBLE_CR}:/root/"
