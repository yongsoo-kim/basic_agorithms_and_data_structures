def find_all_pairs(my_list):
    n = len(my_list)
    possible_pairs = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            pair = "{member1} - {member2}".format(member1=my_list[i], member2=my_list[j])
            possible_pairs.add(pair)

    return possible_pairs


my_list = ["Tom", "Jerry", "Mike"]
print(find_all_pairs(my_list))
