#!/bin/bash
# https://github.com/panda-re/panda/blob/master/panda/docs/PANDA.md : instructions for https://github.com/moyix/panda
# /panda/x86_64-softmmu/panda/plugins/syscalls2

ORIG=$(pwd)
IMG=/var/lib/libvirt/images/fedora20.qcow2
SRC=./sources

virt-copy-in -a $IMG $SRC /root

cd ~/panda/panda/scripts/panda/build/x86_64-softmmu

# change plugin, run ~/panda/build.sh

./qemu-system-x86_64 -net none -drive file=$IMG -m 4096 -enable-kvm -monitor stdio
