#!/bin/bash -eax
# for the packer / vagrant crap...

yum -y install openssh-server || yum -y update openssh-server || true
sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/' /etc/ssh/sshd_config
sed -i 's/#UseDNS no/UseDNS no/' /etc/ssh/sshd_config
sed -i 's/#UsePAM yes/UsePAM yes/' /etc/ssh/sshd_config
systemctl restart sshd

