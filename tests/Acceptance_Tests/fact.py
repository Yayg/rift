import ripe

def fact(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * fact(n-1)

@ripe.Test
def test_fact():
    test_values = [0, 1, 7, 13, 20]
    for i in test_values:
        ret, stdout, stderr = ripe.call(lib.fact, ripe.c_longlong, i)
        if ret != fact(i):
            print("fact({}) = {} != {}".format(i, ret, fact(i)))
            return False
    return True

ripe.init("fact.so")
ripe.run_tests()
