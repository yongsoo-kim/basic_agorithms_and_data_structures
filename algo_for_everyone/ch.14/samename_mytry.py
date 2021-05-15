def find_same_name(a):
    unique_names = set()
    same_names = set()

    for i in a:
        if i not in unique_names:
            unique_names.add(i)
        else:
            same_names.add(i)

    return same_names


name = ["Tom", "Jerry", "Mike", "Tom"]

print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
