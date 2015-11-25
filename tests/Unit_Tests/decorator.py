import ripe

@ripe.Test
def test_decorator():
    print("Passed")

ripe.run_tests()
