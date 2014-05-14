all: bof2

bof2: bof2.c
		gcc -m32 -fno-stack-protector -std=c99 -w $^ -o $@

.PHONY: clean

clean:
		rm bof2
