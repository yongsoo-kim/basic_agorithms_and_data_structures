def sum_num(n):
    if n == 1:
        return 1
    return n + sum_num(n - 1)


print(sum_num(3))
print(sum_num(5))
