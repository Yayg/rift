#! /usr/bin/env python3
from ripe import *

@Test
def test():
    ret, stdout, stderr = ripe.call(lib.segv, ripe.c_int, 0)
    return True

ripe.init("segfault.so")
ripe.run_tests(True)
