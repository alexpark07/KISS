# runing multi-arch binary on x64_86 system

after installing qemu 

``
; arm mode
alex@vm64 $ qemu-arm -L /usr/arm-linux-gnueabi/ ./binary.arm32

; aarch64 mode
alex@vm64 $ qemu-aarch64 -L /usr/aarch64-linux-gnu/ ./binary.arm64
``

That's all. Enjoy
