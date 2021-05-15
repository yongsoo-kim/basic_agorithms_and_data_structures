my_list = [17, 92, 18, 33, 58, 7, 33, 42]

greatest_num = my_list[0]

# 이것도 좋지만...0번째 요소는 건너뛰기 만드는게 아주 조금더 빠를다. 하나 차이지만...
for n in my_list:
    if n > greatest_num:
        greatest_num = n

print(greatest_num)
