CFLAGS=-m32 -std=c99 -fno-stack-protector -ggdb

all: ex_int

ex_int: ex_int.c
		gcc $(CFLAGS) -w $^ -o $@ ; objdump -S $@ -j .text -Mintel > $@.dis

.PHONY: clean

clean:
		rm ex_int
