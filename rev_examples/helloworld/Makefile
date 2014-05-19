all: helloworld

helloworld: helloworld.c
		gcc -m32 -std=c99 -w $^ -o $@ 

.PHONY: clean

clean:
		rm helloworld
