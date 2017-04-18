#!/bin/bash
# http://reverseengineering.stackexchange.com/questions/4738/using-qemu-monitor-interface-to-extract-execution-traces-from-a-binary

#cp *.iso ~/panda/panda/scripts/panda/build/x86_64-softmmu

cd ~/panda/panda/scripts/panda/build/x86_64-softmmu

rm -f floppy
rm -rf /mnt/tmp

dd if=/dev/zero of=floppy bs=1440K count=1
mkfs.ext2 floppy

mkdir /mnt/tmp
mount -o loop ./floppy /mnt/tmp
cp syscalls.c /mnt/tmp/
umount /mnt/tmp

./qemu-system-x86_64 -net none -cdrom ./tinycore.iso -m 1024 -enable-kvm -monitor stdio -panda "syscalls2" -fda ./floppy

# change plugin, run ~/panda/build.sh
