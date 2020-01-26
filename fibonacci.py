def fib(n):
    base = [0, 1]
    a = base[0]
    b = base[1]
    for i in range(n):
        base.append(a+b)
        a = base[i+1]
        b = base[i+2]
    return base[n]

assert fib(2) == 1
assert fib(5) == 5
assert  fib(8) == 21
