CFLAGS=-m32 -std=c99 -fno-stack-protector -ggdb

all: double_pointer

double_pointer: double_pointer.c
		gcc $(CFLAGS) -w $^ -o $@ ; objdump -S $@ -j .text -Mintel > $@.dis

.PHONY: clean

clean:
		rm double_pointer
