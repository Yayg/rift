#! /usr/bin/env python2

from ripe import Test, init, run_tests

@Test
def test_decorator():
    print("Passed")

init("init.so")
run_tests()
