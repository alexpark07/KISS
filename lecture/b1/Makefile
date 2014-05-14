all: bof1

bof1: bof1.c
		gcc -m32 -fno-stack-protector -z execstack -std=c99 -w $^ -o $@

.PHONY: clean

clean:
		rm bof1
