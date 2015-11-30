#! /usr/bin/env python3
from rift import *

@Test
def test():
    ret, stdout, stderr = rift.call(lib.segv, rift.c_int, 0)
    return True

rift.init("segfault.so")
rift.run_tests(True)
