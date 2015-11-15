include Makefile.source

CC=gcc
CFLAGS=
LDFLAGS=-shared -fPIC

%.so: %.c
	$(CC) -o $@ $(LDFLAGS) $^
