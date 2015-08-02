CC   = gcc
ARCH = $(shell getconf LONG_BIT)
FN   = uaf

all: $(FN)

bof1: $(FN).c
ifeq ($(ARCH),64)
	$(CC) -m64 -std=c99 -w $^ -o $@
else
    $(CC) -m32 -std=c99 -w $^ -o $@
endif

.PHONY: clean

clean: 
	rm $(FN)
