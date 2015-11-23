SRCS= $(wildcard *.py)
LIBS= $(SRCS:.py=.so)
TEST_SCRIPTS= $(SRCS:.py=.test)

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
	@$(PYTHON) $^ 1> /dev/null || (echo $^ failed with return code $$? && exit 1);
