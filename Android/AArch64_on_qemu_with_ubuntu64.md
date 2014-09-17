### A Quick'n'Dirty Set-up of an Aarch64 Ubuntu 14.04 VM with QEMU

original link - [http://webkit.sed.hu/blog/](http://webkit.sed.hu/blog/20140816/quickndirty-set-aarch64-ubuntu-1404-vm-qemu)

#### Build your own QEMU/Aarch64

```
sudo apt-get build-dep qemu # install the dependencies
git clone git://git.qemu.org/qemu.git # get the source (at the time of writing, HEAD was at revision 69f87f713069f1f70f86cb65883f7d43e3aa21de)
cd qemu
./configure --target-list=aarch64-softmmu --enable-virtfs # configure for aarch64 (virtfs only needed if you'd like to mount up a dir of the host in the guest OS)
make # build qemu (make install is not necessary)
```

#### Create a clean Aarch64 Ubuntu Core 14.04.1 image

File link - [arm64-prepare-image-qemu.sh](http://webkit.sed.hu/sites/webkit.sed.hu/files/arm64-prepare-image-qemu.txt)

```
wget "http://cdimage.ubuntu.com/ubuntu-core/releases/14.04/release/ubuntu-core-14.04.1-core-arm64.tar.gz"
./arm64-prepare-image-qemu.sh ubuntu-core-14.04.1-core-arm64.tar.gz # the script will sudo!
```

#### Get your hands on suitable kernel & initrd (for those who are lazy to build their own)

```
sudo apt-get install qemu-utils # install tools required to deal with the QCOW2 format
wget "http://cloud-images.ubuntu.com/releases/14.04/release/ubuntu-14.04-server-cloudimg-arm64-disk1.img" # download the cloud image
```

```
sudo modprobe nbd max_part=63
sudo qemu-nbd -c /dev/nbd0 ubuntu-14.04-server-cloudimg-arm64-disk1.img
mkdir mnt
sudo mount /dev/nbd0p1 mnt
```

```
sudo cp mnt/boot/vmlinuz-3.13.0-32-generic .
sudo cp mnt/boot/initrd.img-3.13.0-32-generic .
```

```
sudo umount mnt
sudo qemu-nbd -d /dev/nbd0
rmdir mnt
```

#### Run your brand new Aarch64 Ubuntu 14.04.1 system

```
./aarch64-softmmu/qemu-system-aarch64 -machine virt -cpu cortex-a57 -nographic -smp 1 -m 256 \
        -global virtio-blk-device.scsi=off -device virtio-scsi-device,id=scsi \
        -drive file=../qemu-images/ubuntu-core-14.04.1-core-arm64.img,id=coreimg,cache=unsafe,if=none -device scsi-hd,drive=coreimg \
        -kernel ../qemu-images/vmlinuz-3.13.0-35-generic \
        -initrd ../qemu-images/initrd.img-3.13.0-35-generic \
        -netdev user,id=unet -device virtio-net-device,netdev=unet \
        -net nic -net user,hostfwd=tcp:0.0.0.0:2222-10.0.2.15:22 -nographic \
        --append "console=ttyAMA0 root=/dev/sda"
```

### Customization

So, all the above is OK, so-so, but not exactly what you want. Then, you may want to:

change the size of the disk image holding the root fs: change the count=32768 argument of dd in the arm64-prepare-image-qemu script (specify size in MB).

change the memory allocated for the VM: change the -m 4096 command line parameter of qemu-system-aarch64 (specify size in MB).
replace the default user networking (slirp) with a more powerful networking setup: experiment with the -netdev command line options.

build your own kernel & initrd: good luck with that :)

### Network stuff

[Link Here](http://anddev.tistory.com/category/Virtualization)

``sudo apt-get install bridge-utils uml-utilities``

```
#
# /etc/network/interfaces
#

#기존 eth0의 설정을 주석처리합니다.
#auto eth0
#iface eth0 inet dhcp 

#br0 설정에 dhcp의 네트워크 설정을 추가합니다.
#현재 예에서는 dhcp를 사용하고 있기 때문에 별다른 추가 옵션이 없지만
#정적 IP를 사용하고 있다면 eth0의 정적 IP 옵션(address, gateway 등)을 br0 옵션에 추가해주면 됩니다.
auto br0
iface br0 inet dhcp
    bridge_ports eth0
    bridge_stp off
    bridge_maxwait 0
    bridge_fd 0 
```

```
# brctl addbr br0
# /etc/init.d/networking restart
```

```
#
#  /etc/qemu-ifup-br 
#
#!/bin/sh

set -x

switch=br0

if [ -n "$1" ];then
        /usr/bin/sudo /usr/sbin/tunctl -u `whoami` -t $1
        /usr/bin/sudo /sbin/ip link set $1 up
        sleep 0.5s
        /usr/bin/sudo /sbin/brctl addif $switch $1
        exit 0
else
        echo "Error: no interface specified"
        exit 1
fi
```

```
# run.sh

#!/bin/sh
MAC=`printf 'DE:AD:BE:EF:%02X:%02X\n' $((RANDOM%256)) $((RANDOM%256))`

./aarch64-softmmu/qemu-system-aarch64 -machine virt -cpu cortex-a57 -nographic -smp 1 -m 256 \
        -global virtio-blk-device.scsi=off -device virtio-scsi-device,id=scsi \
        -drive file=../qemu-images/ubuntu-core-14.04.1-core-arm64.img,id=coreimg,cache=unsafe,if=none -device scsi-hd,drive=coreimg \
        -kernel ../qemu-images/vmlinuz-3.13.0-35-generic \
        -initrd ../qemu-images/initrd.img-3.13.0-35-generic \
        -device virtio-net-device,netdev=net0,mac=$MAC -netdev tap,id=net0,script=/etc/qemu-ifup-br \
        -append "console=ttyAMA0 root=/dev/sda"
        
```
