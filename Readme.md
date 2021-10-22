# Browserless- Ansible ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo")
### Introduction To browserless



Browserless Web is communication between web applications without the need for a web browser. The term was coined in an article by Network World, referring mainly to business-to-business interaction.
[Click-Here To Know More](https://github.com/browserless/chrome)
# Browserless installation Using Ansible

* Create Connection with 'root user' of the server from client machine using ssh
```sh
Command:   $ ssh root@<serveripaddress>  -p 5190  
```

* Update the inventory file with 'Server ip address'

* Run ansible using the command 
```sh
syntax:   ansible-playbook -i <inventoryfiename> <ymlfile name> 
```
Example:
```sh
ansible-playbook -i inventory playbook.yml 

```


# Inventory File Explanation

Syntax
```sh
[browserless]
XXX.XXX.XXX.XXX your ip address
[browserless:vars]
ansible_user= username
ansible_port= Port number
browserless_dir= Installation directory of browserless
browserless_user= Username of browserless
browserless_group= Browserless groupname
max_concurrent_sessions= The number of concurrent sessions as a percentage of maximum concurrent sessions.
```
Example file
```sh
[browserless]
158.69.xx.22
[browserless:vars]
ansible_user=ubuntu
ansible_port=5100
browserless_dir=/opt/browserless
browserless_user=browserless
browserless_group=browserless
max_concurrent_sessions=50
.
```






