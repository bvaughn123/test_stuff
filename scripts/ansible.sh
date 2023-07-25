#!/bin/bash -eux

## More for the packr vagrnt stuff..

# chek if ansible is installed
if [ -f /usr/bin/ansible ]; then
    echo "Ansible is already installed"
    exit 0
else: 
# Install Ansible.
yum -y install ansible
fi

# Install EPEL if not already installed
if [ -f /etc/yum.repos.d/epel.repo ]; then
    echo "EPEL is already installed"
    exit 0
else:
    yum -y install epel-release
fi