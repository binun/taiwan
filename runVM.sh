#!/bin/bash
# https://github.com/panda-re/panda/blob/master/panda/docs/PANDA.md : instructions for https://github.com/moyix/panda
#https://www.ibm.com/developerworks/library/l-kvm-libvirt-audit/
#apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
# www.linux-kvm.org/page/Perf_events
#http://www.linux-kvm.org/page/Perf_events#Using_copies_of_guest_files
ORIG=$(pwd)
IMG=/var/lib/libvirt/images/fedora20.qcow2
SRC=./sources

virt-copy-in -a $IMG $SRC /root

cd ~/panda/build/x86_64-softmmu

# change plugin, run ~/panda/build.sh

./qemu-system-x86_64 -net none -drive file=$IMG -m 4096 -enable-kvm -monitor stdio & >> file.txt 2>&1
