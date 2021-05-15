#
def search_list(a, target):
    n = len(a)
    found_indices = []

    for i in range(n):
        if a[i] == target:
            found_indices.append(i)

    return found_indices


v = [17, 92, 18, 33, 58, 7, 33, 42]

print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
