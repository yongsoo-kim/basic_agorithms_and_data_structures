# 입력 리스트안에서 직접 순서를 바꾸는 방식.

# a -> 입력리스트
# 리스트 a의 어디어서(start) 어디까지(end) 정렬 대상인지.
def quick_sort_sub(a, start, end):
    if end - start < 0:
        return

    # 기준값을 정하고 그 기준값에 맞춰 리스트안에서 각 자료의 위치를 맞춤.
    # [기분값보다 작은 값들, 기준값, 기준값보다 큰 값들]
    pivot = a[end]

    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]

    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)


def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)
