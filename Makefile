all:
	$(MAKE) -C gui


clean:
	$(MAKE) -C gui clean

re: clean all
	