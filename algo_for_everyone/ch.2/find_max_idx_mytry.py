def find_max_idx(a):
    n = len(a)

    # max_idx를 알렴 max_v를 표시 안해도 된다. 개인적으로는 내가쓴게 더 이해하기 편하다.
    max_v = a[0]
    max_idx = 0

    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
            max_idx = i

    return max_idx


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(v))
