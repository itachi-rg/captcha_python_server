# Rhel 6

## Setup Yum repository

```
cd /etc/yum.repos.d

wget http://public-yum.oracle.com/RPM-GPG-KEY-oracle-ol6 -O /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle

gpg --quiet --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle

wget http://public-yum.oracle.com/public-yum-ol6.repo

vi public-yum-ol6.repo 

```

## Make repo folder

```
mkdir /repo

chmod 777 /repo/

cd /repo
```
## Swithc off firewall
```
service iptables save

service iptables stop

chkconfig iptables off
```
## Install Conda python
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
## If ipV6 is not connecting, try changing to ipV4 in wgetrc file
```
vi /etc/wgetrc 

chmod 777 Miniconda3-latest-Linux-x86_64.sh 

./Miniconda3-latest-Linux-x86_64.sh 
```

## Flask for server

`pip install flask`

## Clone the captcha_server from github

` `

## Generate privateKey.key and cert.crt

`openssl req -x509 -newkey rsa:4096 -keyout privateKey.key -out cert.crt -days 3650`

But this will ask for passphrase everytime the server is launched. Remove the passphrase using 

`openssl rsa -in privateKey.key -out privateKey.key`

## Run server
```
python server.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Ensure that it is running on '0.0.0.0' to be visible to external network

```
## Git setup
```
yum update git

git config --global user.name "itachi-rg"

git config --global user.email rohan.gangaraju@gmail.com

#Forbidden message shown when https is not used 
#[root@rg-001-rhel6-u8 captcha_server]# git push -u origin master
#error: The requested URL returned error: 403 Forbidden while accessing https://github.com/itachi-rg/captcha_python_server.git/info/refs

## Use set-url with your username 

git remote set-url origin https://itachi-rg@github.com/itachi-rg/captcha_python_server.git
```
## Ensure credentials are stored persistently
```
git config credential.helper store

#Error when password prompt for GUI is launched, uset SSH_ASKPASS to allow command line entry of password
#[root@rg-001-rhel6-u8 captcha_server]# git push 
#(gnome-ssh-askpass:17556): Gtk-WARNING **: cannot open display: 

unset SSH_ASKPASS
```
## Setup NN project

`git clone -b captcha_image_class https://github.com/itachi-rg/captcha.git captcha_nn`

## Python package installations for numpy, opencv
```
conda install scipy

conda install scikit-learn

pip install opencv-python

pip install opencv-contrib-python

conda install dill

conda install lxml

```

## Add the following files from the captcha NN 

Python scripts 
``` 
captcha_model_build.py
neurallib.py
captcha_pre_process.py
```

Data files
```
image_class_dictionary.pkl
temp_data.pkl
```


## Finally run the server in the background
```
nohup python server.py &
```


