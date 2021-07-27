# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
$script= <<-SCRIPT
sed -i s/SELINUX=enforcing/SELINUX=permissive/ /etc/selinux/config

yum install -y epel-release

rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key

yum install -y java-1.8.0-openjdk-devel curl git wget ansible openssh-server


sed -i s/#PubkeyAuthentication/PubkeyAuthentication/ /etc/ssh/sshd_config
sed -i s/#PasswordAuthentication/PasswordAuthentication/ /etc/ssh/sshd_config 

curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo

yum install -y jenkins

systemctl enable jenkins
systemctl start jenkins

if [ -e /var/lib/jenkins/secrets/initialAdminPassword ];then
	cat /var/lib/jenkins/secrets/initialAdminPassword 
fi

# wget -O- get.docker.com | bash


SCRIPT

$scr= <<-SCRIPT2

sed -i s/SELINUX=enforcing/SELINUX=permissive/ /etc/selinux/config

yum install -y epel-release

yum install -y java-1.8.0-openjdk-devel curl wget anisble git python3 python3-pip

useradd jenkins

sed -i s/#PubkeyAuthentication/PubkeyAuthentication/ /etc/ssh/sshd_config
sed -i s/#PasswordAuthentication/PasswordAuthentication/ /etc/ssh/sshd_config
sed -i s/PasswordAuthentication\ no/#PasswordAuthentication\ no/ /etc/ssh/sshd_config

systemctl restart sshd
 
wget -O- get.docker.com | bash

systemctl start docker
sudo usermod -aG docker $USER


SCRIPT2





Vagrant.configure("2") do |config|
config.vm.define "jenkins" do |jenkins|
 	 jenkins.vm.box="centos/7"
	 jenkins.vm.hostname="jenkins-ci"
	 jenkins.vm.network "private_network", ip: "10.100.101.102"
  	 jenkins.vm.network "forwarded_port", guest: 8080, host: 8080
         jenkins.vm.provision "shell", inline: $script
	end
  config.vm.define "j" do|j|
 	 j.vm.box="centos/7"
	 j.vm.hostname="jenkins-worker"
	 j.vm.network "private_network", ip: "10.100.101.103"
         j.vm.provision "shell", inline: $scr
	end


end
