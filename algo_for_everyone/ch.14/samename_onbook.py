def find_same_name(a):
    # 1단계: 각 이름이 등장한 횟수를 딕셔너리로 만듬.
    name_dict = {}

    for name in a:
        # 만일 이름이 딕셔러니 안에 발견되면 등장 횟수를 1 증가.
        if name in name_dict:
            name_dict[name] = name_dict[name] + 1
        # 그게 아니라면 초기 등장횟수(1)을 저장
        else:
            name_dict[name] = 1

    result = set()

    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result


names = ["Tom", "Jerry", "Mike", "Tom"]

print(find_same_name(names))

names2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(names2))
