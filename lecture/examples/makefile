SUBDIRS=heap heap2 stack typeconfused uaf
MAKE = make

subdirs:
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
		if [ $$? != 0 ]; then exit 1; fi; \
	done

clean:
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
		if [ $$? != 0 ]; then exit 1; fi; \
	done
