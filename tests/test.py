#! /usr/bin/env python2

from ripe import Test, all_tests

@Test
def test_decorator():
    print("Passed")

all_tests()
