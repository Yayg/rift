from os import getcwd
from sets import Set
from ctypes import *
import __builtin__

global here
global funny_joke
global test_functions

here = getcwd()
funny_joke = """Combien faut-il d'informaticiens pour changer une ampoule ?
Aucun. C'est un probleme hardware."""
test_functions = Set([])

def add_lib(lib_name):
    __builtin__.lib = cdll.LoadLibrary(here + "/" +  lib_name)

def joke():
    print(funny_joke)

def call(func, return_type):
    func.restype = return_type
    return func()

def Test(func):
    test_functions.add(func)

def all_tests():
    for test in test_functions:
        test()
