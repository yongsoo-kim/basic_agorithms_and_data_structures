student_info_dict = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}


def find_student(code):
    student_name = student_info_dict.get(code, "?")
    return student_name


print(find_student(39))
print(find_student(14))
print(find_student(100))
