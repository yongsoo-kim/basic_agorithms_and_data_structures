# 선택정렬. 시간 복잡도는 O(n^2).
# 여기서는 쉽게 풀어써본다.
def find_min_idx(a):
    min_idx = 0
    n = len(a)

    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i

    return min_idx


def sel_sort(a):
    result = []

    while a:
        # 제일 작은 요소를 찾기.
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)

    return result


d = [2, 4, 5, 1, 3]

print(sel_sort(d))
