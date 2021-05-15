# 선택정렬. 시간 복잡도는 O(n^2).
# 여기서는 자리바꿈을 선보인다. "서로 다른 두수를 비교한다" 라는 점에서 ch.3의 동명이인 비교와 유사한면이 있다.

def sel_sort(a):
    n = len(a)
    # 마지막 요소는 비교할 필요가 없다.
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                # 이것도 된다. 자바에서는 특히.
                # temp = a[i]
                # a[i] = a[j]
                # a[j] = temp

                # 파이썬 적인 방식....
                a[j], a[i] = a[i], a[j]

    return a


d = [2, 4, 5, 1, 3]

print(sel_sort(d))
