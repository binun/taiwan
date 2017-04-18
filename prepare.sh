
apt-get install -y qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils
# https://linuxconfig.org/simple-virtualization-with-ubuntu-16-04-and-kvm
# https://askubuntu.com/questions/179508/kvm-bridged-network-not-working
git clone https://github.com/panda-re/panda.git
add-apt-repository ppa:phulin/panda
apt-get -y update
apt-get build-dep qemu
apt-get install -y python-pip git protobuf-compiler protobuf-c-compiler \
  libprotobuf-c0-dev libprotoc-dev libelf-dev \
  libcapstone-dev libdwarf-dev python-pycparser llvm-3.3 clang-3.3 libc++-dev
mkdir -p build-panda && cd build-panda
~/panda/panda/scripts/install_ubuntu.sh
ln /root/panda/panda/scripts/panda/build/x86_64-softmmu/qemu-system-x86_64 qemu
