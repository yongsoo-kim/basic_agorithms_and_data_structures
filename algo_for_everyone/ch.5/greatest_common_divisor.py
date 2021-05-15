def gcd(a, b):
    temp_gcd = min(a, b)
    while True:
        if a % temp_gcd == 0 and b % temp_gcd == 0:
            return temp_gcd
        else:
            temp_gcd = temp_gcd - 1


print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))
