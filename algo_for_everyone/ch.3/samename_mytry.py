def find_same_name(names):
    n = len(names)
    same_names = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if names[i] == names[j]:
                same_names.add(names[j])

    return same_names


names = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(names))
