/etc/qemu-ifup tap0
qemu-system-x86_64 -boot c -cdrom tinycore.iso -m 1024 -net nic -net tap,ifname=tap0,script=no,downscript=no
