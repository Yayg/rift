import rift

def fact(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * fact(n-1)

@rift.Test
def test_fact():
    test_values = [0, 1, 7, 13, 20]
    for i in test_values:
        ret, stdout, stderr = rift.call(lib.fact, rift.c_longlong, i)
        if ret != fact(i):
            print("fact({}) = {} != {}".format(i, ret, fact(i)))
            return False
    return True

rift.init("fact.so")
rift.run_tests()
