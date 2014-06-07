CFLAGS=-m32 -std=c99 -fno-stack-protector -ggdb

all: pointer_dim

pointer_dim: pointer_dim.c
		gcc $(CFLAGS) -w $^ -o $@ ; objdump -S $@ -j .text -Mintel > $@.dis

.PHONY: clean

clean:
		rm pointer_dim
