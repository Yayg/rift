SRCS= $(wildcard *.py)
LIBS= $(SRCS:.py=.so)
TEST_SCRIPTS= $(SRCS:.py=.test)

ifndef TRAVIS_PYTHON_VERSION
    PYTHON = python2.7
else
    PYTHON = python$(TRAVIS_PYTHON_VERSION)
endif


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
