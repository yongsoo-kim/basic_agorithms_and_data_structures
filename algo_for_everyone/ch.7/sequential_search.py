# 순차 탐색.
def search_list(a, target):
    n = len(a)

    for i in range(n):
        if a[i] == target:
            return i

    return -1


# 정렬되어 있지 않는 배열.
v = [17, 92, 18, 33, 58, 7, 33, 42]

print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
