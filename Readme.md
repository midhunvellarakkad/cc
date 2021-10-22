
# Browserless- Ansible ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo")
### Introduction To browserless



Browserless Web is communication between web applications without the need for a web browser. The term was coined in an article by Network World, referring mainly to business-to-business interaction.
[Click-Here To Know More](https://github.com/browserless/chrome)
# Browserless installation Using Ansible.

### -   Browserless-Ansible folder will Contain The Following files
*   inventory
*   playbook.yml
*   systemd_browserless_service
*   env_dev
*   .gitignore 

### -   Installation Steps

*   Create inventory file using 
 ```sh
command: $  nano inventory
```

* Update the inventory file with 'Server ip address''Port number ' etc
 ```sh
[browserless]
172.16.XXX.XXX                                               (Enter Your Private ip address)
[browserless:vars]
ansible_user=ubuntu                                          (a user in server)
ansible_port=5190                                            (port number of ssh)
browserless_dir=/opt/browserless                             (Installation directory of browserless)
browserless_user=browserless                                (Username of browserless)
browserless_group=browserless                                (Browserless groupname)
max_concurrent_sessions=50                                  (The number of concurrent sessions)
```


* Run ansible using the command 
```sh
syntax:   ansible-playbook -i <inventoryfiename> <playbookfile name> 
```
Example:
```sh
ansible-playbook -i inventory playbook.yml 

```


# Inventory File Explanation

Syntax
```sh
[browserless]
XXX.XXX.XXX.XXX              Your ip address
[browserless:vars]
ansible_user=               username
ansible_port=               Port number
browserless_dir=             Installation directory of browserless
browserless_user=           Username of browserless
browserless_group=          Browserless groupname
max_concurrent_sessions=    The number of concurrent sessions as a percentage of maximum concurrent sessions.
```
Example file
```sh
[browserless]
172.16.xx.xx (Private ip address of server)
[browserless:vars]
ansible_user=ubuntu (a user in server)
ansible_port=5100 (port number of ssh)
browserless_dir=/opt/browserless
browserless_user=browserless
browserless_group=browserless
max_concurrent_sessions=50

```

# About -   Systemd_browserless_service 

By Running playbook file , the 'Systemd_browserless_service' will be copied to the destination '/etc/systemd/system/browserless.service'.

```sh
[Unit]
Description=Browserless
[Service]
Restart=always
RestartSec=10
Environment=ENABLE_CORS=true
Environment=DEBUG=browserless*
Environment=FUNCTION_BUILT_INS='["*"]'
Environment=FUNCTION_EXTERNALS=true
Environment=HOST={{ ansible_ens4.ipv4.address }}                    (Ip Address of Host Machine)
Environment=PORT=3000                                               (Browserless service running port)
Environment=PREBOOT_CHROME=false
Environment=MAX_QUEUE_LENGTH=100
Environment=CONNECTION_TIMEOUT=900000
Environment=CHROME_REFRESH_TIME=1200000
Environment=MAX_CONCURRENT_SESSIONS={{ max_concurrent_sessions }}
Environment=KEEP_ALIVE=true
Environment=CHROME_REFRESH_TIME=sixtyMinutes
Type=simple
User={{ browserless_user }}                                          (Browserless username)
Group={{ browserless_group }}                                        (Browserless Group Name)
WorkingDirectory={{ browserless_dir }}                              (Browserless Directory)
ExecStart=/usr/bin/node  --max-old-space-size=4086  {{ browserless_dir }}/build/index.js (Executional javascript file)
ExecStop=
[Install]
WantedBy=multi-user.target
```





