CFLAGS=-m32 -std=c99 -fno-stack-protector -ggdb

all: simple_bof 

simple_bof: simple_bof.c
		gcc $(CFLAGS) -w $^ -o $@ ; objdump -S $@ -j .text -Mintel > $@.dis

.PHONY: clean

clean:
		rm simple_bof
