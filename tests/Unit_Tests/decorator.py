import rift

@rift.Test
def test_decorator():
    print("Passed")

rift.run_tests()
