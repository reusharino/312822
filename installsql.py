import subprocess,os,sys,random,time,urllib2,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

'''
_____________________________________________________
                INSTALLING MYSQL
_____________________________________________________
'''
time.sleep(5)

run("apt-get update -y")
run("apt-get upgrade -y")
run("apt-get install -y sudo")

run("apt-get install gnupg -y")
run("cd /tmp")
run("wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb --allow-insecure-repositories")
run("sudo dpkg -i mysql-apt-config*")
run("sudo apt update -y")
run("sudo apt install mysql-server")
run("sudo systemctl status mysql")
run("mysql_secure_installation")
