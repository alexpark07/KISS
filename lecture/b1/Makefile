CC   = gcc
ARCH = $(shell getconf LONG_BIT)

all: bof1

bof1: bof1.c
ifeq ($(ARCH),64)
		$(CC) -m64 -fno-stack-protector -z execstack -std=c99 -w $^ -o $@
else
		$(CC) -m32 -fno-stack-protector -z execstack -std=c99 -w $^ -o $@
endif

.PHONY: clean

clean:
		rm bof1
