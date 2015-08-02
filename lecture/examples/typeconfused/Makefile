CC   = gcc
ARCH = $(shell getconf LONG_BIT)
FN   = typeconfused

all: $(FN)

bof1: $(FN).cc
ifeq ($(ARCH),64)
	$(CC) -m64 -fno-stack-protector -z execstack -std=c99 -w $^ -o $@
else
    $(CC) -m32 -fno-stack-protector -z execstack -std=c99 -w $^ -o $@
endif

.PHONY: clean

clean: 
	rm $(FN)
