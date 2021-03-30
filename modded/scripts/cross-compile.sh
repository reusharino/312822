#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo -n "Install mysql-server and mysql-client (y/n)? "
old_stty_cfg=$(stty -g)
stty raw -echo
answer=$( while ! head -c 1 | grep -i '[ny]' ;do true ;done )
stty $old_stty_cfg
if echo "$answer" | grep -iq "^y" ;then
    echo "Installing mysql..."
    apt-get install -y mysql-server mysql-client
fi

echo -n "Installing gcc, golang, electric-fence..."
apt-get install -y gcc golang electric-fence

echo "Creating folder /etc/xcompile"
mkdir /etc/xcompile
cd /etc/xcompile
echo "Delete all file in this folder"
rm -rf *

echo
echo "Download cross-compiler-armv4l.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2
echo "Download cross-compiler-armv5l.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv5l.tar.bz2
echo "Download cross-compiler-armv6l.tar.bz2"
wget http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2
echo "Download cross-compiler-i586.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2
echo "Download cross-compiler-m68k.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2
echo "Download cross-compiler-mips.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2
echo "Download cross-compiler-mipsel.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2
echo "Download cross-compiler-powerpc.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2
echo "Download cross-compiler-sh4.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2
echo "Download cross-compiler-sparc.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2
echo "Download cross-compiler-i686.tar.bz2"
wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i686.tar.bz2

echo "extracting cross-compiler-armv4l.tar.bz2 ..."
tar -jxf cross-compiler-armv4l.tar.bz2
echo "extracting cross-compiler-armv5l.tar.bz2 ..."
tar -jxf cross-compiler-armv5l.tar.bz2
echo "extracting cross-compiler-armv6l.tar.bz2 ..."
tar -jxf cross-compiler-armv6l.tar.bz2
echo "extracting cross-compiler-i586.tar.bz2 ..."
tar -jxf cross-compiler-i586.tar.bz2
echo "extracting cross-compiler-m68k.tar.bz2 ..."
tar -jxf cross-compiler-m68k.tar.bz2
echo "extracting cross-compiler-mips.tar.bz2 ..."
tar -jxf cross-compiler-mips.tar.bz2
echo "extracting cross-compiler-mipsel.tar.bz2 ..."
tar -jxf cross-compiler-mipsel.tar.bz2
echo "extracting cross-compiler-powerpc.tar.bz2 ..."
tar -jxf cross-compiler-powerpc.tar.bz2
echo "extracting cross-compiler-sh4.tar.bz2 ..."
tar -jxf cross-compiler-sh4.tar.bz2
echo "extracting cross-compiler-sparc.tar.bz2 ..."
tar -jxf cross-compiler-sparc.tar.bz2
echo "extracting cross-compiler-i686.tar.bz2 ..."
tar -jxf cross-compiler-i686.tar.bz2

echo "removing all tar.bz2 from /etc/xcompile ..."
rm *.tar.bz2
echo "move cross-compiler-armv4l to armv4l ..."
mv cross-compiler-armv4l armv4l
echo "move cross-compiler-armv5l to armv5l ..."
mv cross-compiler-armv5l armv5l
echo "move cross-compiler-armv6l to armv6l ..."
mv cross-compiler-armv6l armv6l
echo "move cross-compiler-i586 to i586 ..."
mv cross-compiler-i586 i586
echo "move cross-compiler-m68k to m68k ..."
mv cross-compiler-m68k m68k
echo "move cross-compiler-mips to mips ..."
mv cross-compiler-mips mips
echo "move cross-compiler-mipsel to mipsel ..."
mv cross-compiler-mipsel mipsel
echo "move cross-compiler-powerpc to powerpc ..."
mv cross-compiler-powerpc powerpc
echo "move cross-compiler-sh4 to sh4 ..."
mv cross-compiler-sh4 sh4
echo "move cross-compiler-sparc to sparc ..."
mv cross-compiler-sparc sparc
echo "move cross-compiler-i686 to i686 ..."
mv cross-compiler-i686 i686

echo "export PATH ..."
export PATH=$PATH:/etc/xcompile/armv4l/bin
export PATH=$PATH:/etc/xcompile/armv6l/bin
export PATH=$PATH:/etc/xcompile/i586/bin
export PATH=$PATH:/etc/xcompile/m68k/bin
export PATH=$PATH:/etc/xcompile/mips/bin
export PATH=$PATH:/etc/xcompile/mipsel/bin
export PATH=$PATH:/etc/xcompile/powerpc/bin
export PATH=$PATH:/etc/xcompile/powerpc-440fp/bin
export PATH=$PATH:/etc/xcompile/sh4/bin
export PATH=$PATH:/etc/xcompile/sparc/bin
export PATH=$PATH:/etc/xcompile/armv5l/bin
export PATH=$PATH:/etc/xcompile/i686/bin

echo "get go-sql-driver"
go get github.com/go-sql-driver/mysql
echo "go-shellwords"
go get github.com/mattn/go-shellwords

echo "export PATH go-sql-driver"
export PATH=$PATH:/usr/local/go/bin
echo "export PATH go-shellwords"
export GOPATH=$HOME/Documents/go
