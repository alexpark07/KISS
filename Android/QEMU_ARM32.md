http://daehee87.tistory.com/282

http://www.routards.org/2013/08/defcon-21-ctf-binaries-and-environment.html

```
#!/bin/sh

#wget http://odroid.us/odroid/users/osterluk/qemu-example/qemu-example.tgz
#tar zxf qemu-example.tgz ./zImage
#rm -f qemu-example.tgz

#wget http://releases.linaro.org/12.04/ubuntu/precise-images/developer/linaro-precise-developer-20120426-86.tar.gz
#tar zxf linaro-precise-developer-20120426-86.tar.gz 
#rm -f linaro-precise-developer-20120426-86.tar.gz

qemu-img create -f raw rootfs.img 8G
mkfs.ext3 rootfs.img
mkdir mnt
mount -o loop rootfs.img mnt
rsync -a binary/boot/filesystem.dir/ mnt/
umount mnt
```

```
#!/bin/sh

./qemu-system-arm -M vexpress-a9 -m 512 -kernel zImage -sd rootfs.img \
    -append "root=/dev/mmcblk0 rw physmap.enabled=0 console=ttyAMA0" \
    -net nic -net user,hostfwd=tcp:0.0.0.0:2222-10.0.2.15:22 -nographic
```
