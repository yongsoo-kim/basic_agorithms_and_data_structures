def find_biggest(input_list, n):
    if n == 1:
        return input_list[0]
    # 제일 마지막건 제하고 그전의 물건들중 최대를 찾는다.
    max_n_1 = find_biggest(input_list, n - 1)
    if max_n_1 > input_list[n - 1]:
        return max_n_1
    else:
        return input_list[n - 1]


my_list = [3, 23, 5, 7, 11, 9]

print(find_biggest(my_list, len(my_list)))
