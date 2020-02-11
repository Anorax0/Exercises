"""Just for practice"""


def fib(start=0):
    """
    Fibonacci function
    :param start: int
    :return: int
    """
    base = [0, 1]
    base_a = base[0]
    base_b = base[1]
    for i in range(start):
        base.append(base_a+base_b)
        base_a = base[i+1]
        base_b = base[i+2]
    return base[start]


assert fib(2) == 1
assert fib(5) == 5
assert fib(8) == 21
