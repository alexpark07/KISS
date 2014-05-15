all: bof4

bof4: bof4.c
		gcc -m32 -std=c99 -w $^ -o $@ -z execstack

.PHONY: clean

clean:
		rm bof4
