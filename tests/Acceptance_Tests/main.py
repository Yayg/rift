#! /usr/bin/env python2
import ripe

ripe.init("main.so")
print(ripe.call(lib.main, ripe.c_int))
