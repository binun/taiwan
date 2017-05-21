
apt-get install -y qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils
apt-get install -y libguestfs-tools
# https://linuxconfig.org/simple-virtualization-with-ubuntu-16-04-and-kvm
# https://askubuntu.com/questions/179508/kvm-bridged-network-not-working
git clone https://github.com/panda-re/panda.git
add-apt-repository ppa:phulin/panda
apt-get -y update
apt-get build-dep qemu
apt-get install -y python-pip git protobuf-compiler protobuf-c-compiler \
  libprotobuf-c0-dev libprotoc-dev libelf-dev \
  libcapstone-dev libdwarf-dev python-pycparser llvm-3.3 clang-3.3 libc++-dev

#wget https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Live/x86_64/Fedora-Live-LXDE-x86_64-20-1.iso -O Fedora.iso 

# https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Virtualization_Deployment_and_Administration_Guide/sect-troubleshooting-systemtaptrace.html
# https://vmsplice.net/~stefan/stefanha-tracing-summit-2014.pdf
# https://events.linuxfoundation.org/images/stories/pdf/lcjp2012_guangrong.pdf
# https://psuriset.com/2015/07/09/trace-system-calls-using-perf/
