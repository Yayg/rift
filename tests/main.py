#! /usr/bin/env python2

import ripe

ripe.add_lib("main.so")
print(ripe.call(lib.main, ripe.c_int))
