#!/bin/bash

rm -f floppy
rm -rf /mnt/tmp

dd if=/dev/zero of=floppy bs=5M count=1
mkfs.ext2 floppy
mkdir /mnt/tmp
mount -o loop floppy /mnt/tmp

cp malware/*.zip /mnt/tmp
cp deflate.sh /mnt/tmp
umount /mnt/tmp

qemu-system-x86_64 -boot c -net none -cdrom puppy.iso -m 2048 -fda ./floppy


