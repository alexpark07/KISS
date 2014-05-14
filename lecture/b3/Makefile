all: bof3

bof3: bof3.c
		gcc -m32 -fno-stack-protector -std=c99 -w $^ -o $@

.PHONY: clean

clean:
		rm bof3
