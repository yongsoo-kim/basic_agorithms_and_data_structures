def find_fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return find_fibonacci(n - 2) + find_fibonacci(n - 1)


print(find_fibonacci(1))
print(find_fibonacci(2))
print(find_fibonacci(3))
print(find_fibonacci(4))
print(find_fibonacci(5))
