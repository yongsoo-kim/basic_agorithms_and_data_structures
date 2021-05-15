def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    # 그룹은 나누어 각각 병합 정렬을 호출하는 과정.
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    # 두 그룹을 하나로 병합
    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 아직 남아있는 자료들을 결과에 추가.
    while g1:
        result.append(g1.pop(0))

    while g2:
        result.append(g2.pop(0))

    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))
