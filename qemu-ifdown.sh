#!/bin/sh 
# 
# Script to bring down and delete bridge br0 when QEMU exits 
# 
# Bring down eth0 and br0 
#
/sbin/ifdown eth0
/sbin/ifdown br0
/sbin/ifconfig br0 down 
# 
# Delete the bridge
#
/usr/sbin/brctl delbr br0 
# 
# bring up eth0 in "normal" mode 
#
/sbin/ifconfig eth0 -promisc
/sbin/ifup eth0 
#
# delete the tap device
#
/usr/sbin/openvpn --rmtun --dev $1
