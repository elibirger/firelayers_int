Content:

Ansible scripts:
####
vagrant up will set 2 apache, set index.html with "hello from server <hostname>,and add haproxy

####
add/remove developer usage:

ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory add_developer.yml --extra-vars "user=USERNAME path=PATH_TO_id_rsa.pub"

ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory remove_developer.yml --extra-vars "user=USERNAME path=PATH_TO_id_rsa.pub"

Python scripts:
######
find duplicated files effectively

######
tree command in Python

#####
Query - get all instances tags from AWS S3 using boto ec2
