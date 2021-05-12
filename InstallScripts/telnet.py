import subprocess,os,sys,random,time,urllib3,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

run("telnet 10.10.0.40")
run("user")
run("user")
