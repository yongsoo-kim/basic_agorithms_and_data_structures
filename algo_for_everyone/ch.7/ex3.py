stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]


def find_student_name(snum):
    for i, n in enumerate(stu_no):
        if n == snum:
            return stu_name[i]

    return "?"


print(find_student_name(67))
print(find_student_name(68))
