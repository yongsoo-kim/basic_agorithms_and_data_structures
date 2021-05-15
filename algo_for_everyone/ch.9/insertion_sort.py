# 간단한 삽입 정렬. 일단 하나 빼내고 시작하는게 다르다.


def find_next_ins_idx(a, v):
    n = len(a)
    for i in range(n):
        if a[i] > v:
            return i

    return n


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)  # 기존 리스트에서 한개를 꺼냄
        # 다음에 삽입할 장소 를 알아낸다.
        ins_idx = find_next_ins_idx(result, value)
        # 해당 장소에 삽입한다.
        result.insert(ins_idx, value)

    return result


d = [2, 4, 5, 1, 3]
print(ins_sort(d))
