

## FAIL!!!!!!##
# 인덱스가 반절로 줄어버린다!
def binary_search(a, target):
    # 주어진 탐색 대상이 비어 있다면 탐색할 필요가 없다.
    if len(a) <= 0:
        return -1
    # 찾는 값과 주어진 탐색 대상의 중간 위치 값을 비교합니다.

    mid_idx = len(a) // 2
    if a[mid_idx] == target:
        return mid_idx
    elif a[mid_idx] > target:
        binary_search(a[:mid_idx - 1], target)
    else:
        binary_search(a[mid_idx + 1:], target)


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))
