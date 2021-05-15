def fact(n):
    f = 1
    if n == 0:
        return f
    for i in range(1, n + 1):
        f = f * i

    return f


print(fact(0))
print(fact(1))
print(fact(5))
print(fact(10))
