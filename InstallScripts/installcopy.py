import subprocess,os,sys,random,time,urllib3,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

'''
_____________________________________________________
             INSTALLING GUEST ADDITIONS
_____________________________________________________
'''
time.sleep(5)



run("apt-get install build-essential module-assistant -y")
run("m-a prepare")
run("mount /media/cdrom")
run("sh /media/cdrom/VBoxLinuxAdditions.run")
