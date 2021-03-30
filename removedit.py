import subprocess,os,sys,random,time,urllib3,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

run("mkdir edit")
run("mkdir edit/bot")
run("mkdir edit/cnc")

run("mv edit/bot/table.c JG/mirai/bot")

run("mv edit/cnc/* JG/mirai/cnc")

run("rm -rf edit")
