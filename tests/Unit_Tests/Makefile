SRCS= $(wildcard *.c)
LIBS= $(SRCS:.c=.so)
PYSRCS= $(wildcard *.py)
TEST_SCRIPTS= $(PYSRCS:.py=.test)

PYTHON = python

CC=gcc
CFLAGS=
LDFLAGS=-shared -fPIC

all: $(LIBS)

%.so: %.c
	$(CC) -o $@ $(LDFLAGS) $^

tests: $(TEST_SCRIPTS)

%.test: %.py
	$(info Launching $^ with $(PYTHON))
	@$(PYTHON) $^ || (echo $^ failed with return code $$? && exit 1);

clean:
	rm -rf $(LIBS)
