FROM ubuntu:22.04

# Installer SSH et utilitaires de base
RUN apt update && apt install -y openssh-server python3 sudo && \
    mkdir /var/run/sshd && \
    useradd -m -s /bin/bash ansible && \
    echo "ansible:ansible" | chpasswd && \
    adduser ansible sudo && \
    echo "ansible ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Autoriser le login SSH par mot de passe
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]