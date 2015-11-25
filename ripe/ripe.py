import sys
import os
import __builtin__

from ctypes import *
from cStringIO import StringIO
from termcolor import cprint

import colorama
global here
global test_functions

here = os.getcwd()
test_functions = set([])

# Constant format output strings
success_string  = '[OK] {}'
fail_string     = '[KO] {}'
problem_string  = '[KO] {}: Process exited with error code {}'
success_color   = 'green'
fail_color      = 'red'
print_args      = []
print_success = lambda *args: cprint(success_string.format(*args),
                                     success_color)
print_fail    = lambda *args: cprint(fail_string.format(*args),
                                     fail_color)
print_problem = lambda *args: cprint(problem_string.format(*args),
                                     fail_color)

# Init ripe with lib name
def init(lib_name):
    """lib_name -- name of the .so to load
    """
    colorama.init()
    __builtin__.lib = cdll.LoadLibrary(here + "/" +  lib_name)

# Decorator for functions attempting to be tested
def Test(func):
    """Decorator registering test functions.
    Test function have to return a boolean and can modify the output by
    changing ripe.success_string, ripe.fail_string, ripe.print_args values.
    """
    test_functions.add(func)

# Stdout catching
class _Capturing(list):
    """Capturing capture printed content and add it in itself.
    Use guide:
    with Capturing() as stdout, stderr:
        do_something(my_object)
    """
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = self._stdoutio = StringIO()
        sys.stderr = self._stderrio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend((self._stdoutio.getvalue().splitlines(),
                      self._stderrio.getvalue().splitlines()))
        sys.stdout = self._stdout
        sys.stderr = self._stderr

# Call method that capture return value, stdout and stderr
def call(func, ret_type, *args):
    """call(func, ret_type, *args) -> (ret_value, stdout, stderr)
    Call a fucntion and return it value cast with ret_type and also stdout
    and stderr.
    func     -- function ptr accessible through `lib` global variable.
    ret_type -- return type of the c function (ctypes type)
    """
    ret = None
    stdout = None
    stderr = None
    func.restype = ret_type
    with _Capturing() as streams:
        ret = func(*args)
    return (ret, streams[0], streams[1])

def run_tests(handle_fail=False):
    """Run all tests."""
    for test in test_functions:
        print_args = [test.__name__]
        if handle_fail:
            child_pid = os.fork()
            if child_pid == 0:
                if test():
                    print_success(*print_args)
                else:
                    print_fail(*print_args)
            else:
                _, ret_code = os.waitpid(child_pid, 0)
                if ret_code != 0:
                    print_args.append(ret_code)
                    print_problem(*print_args)
        else:
          if test():
              print_success(*print_args)
          else:
              print_fail(*print_args)
