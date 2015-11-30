#! /usr/bin/env python3
from rift import *

def fact(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * fact(n-1)

@Test
def test_fact_correct():
    test_values = [0, 1, 7, 13, 20]
    for i in test_values:
        ret, stdout, stderr = rift.call(lib.fact, rift.c_longlong, i)
        if ret != fact(i):
            print("fact({}) = {} != {}".format(i, ret, fact(i)))
            return False
    return True

@Test
def test_fact_fail():
    test_values = [0, -1, -7, -13, -20]
    for i in test_values:
        ret, stdout, stderr = rift.call(lib.fact, rift.c_longlong, i)
        if ret != fact(i):
            print("fact({}) = {} != {}".format(i, ret, fact(i)))
            return False
    return True

rift.init("fact.so")
rift.run_tests(True)
