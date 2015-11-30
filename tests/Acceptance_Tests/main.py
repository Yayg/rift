#! /usr/bin/env python2
import rift

rift.init("main.so")
print(rift.call(lib.main, rift.c_int))
