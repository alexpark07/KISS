.SUFFIXES : .c .o
CFLAGS= -Wall -std=gnu99 -O0 -ggdb3
CC=gcc
ARM32CC=arm-linux-gnueabi-gcc
ARM64CC=aarch64-linux-gnu-gcc
OBJDUMP=objdump
ARM32OBJDUMP=arm-linux-gnueabi-objdump
ARM64OBJDUMP=aarch64-linux-gnu-objdump

all: if

if: if.c
		echo "compiling x86 binary"
		$(CC) $(CFLAGS) -m32 -w $^ -o $@.m32 
		$(OBJDUMP) -S $@.m32 -j .text -Mintel | awk '/<main>:/,/c3/' > $@.m32.dis

		echo "compiling x64_86 binary"
		$(CC)  $(CFLAGS) -m64 -w $^ -o $@.m64 
		$(OBJDUMP) -S $@.m64 -j .text -Mintel | awk '/<main>:/,/c3/' > $@.m64.dis

		echo "compiling arm32 binary"
		$(ARM32CC) $(CFLAGS) -w $^ -o $@.arm32
		$(ARM32OBJDUMP) -S $@.arm32 -j .text | awk '/main>:/,/{fp, pc}/' > $@.arm32.dis

		echo "compiling arm64 binary"
		$(ARM64CC) $(CFLAGS) -w $^ -o $@.arm64
		$(ARM64OBJDUMP) -S $@.arm64 -j .text | awk '/main>:/,/ret/' > $@.arm64.dis
.PHONY: clean

clean:
	rm -rf *.m32 *.m64 *.arm32 *.arm64 *.dis
