#!/bin/bash

# 1. Թարմացնում ենք համակարգը
sudo apt update -y && sudo apt upgrade -y

# 2. Տեղադրում ենք Terraform
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
wget -O- https://hashicorp.com | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform -y

# 3. Տեղադրում ենք kubectl
curl -LO "https://k8s.io(curl -L -s https://k8s.io)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# 4. Տեղադրում ենք Docker
sudo apt install docker.io -y
sudo usermod -aG docker $USER

# 5. Տեղադրում ենք Ansible
sudo apt install ansible -y

echo "Բոլոր գործիքները տեղադրված են: Խնդրում եմ վերամիանալ (reconnect) SSH-ին:"
