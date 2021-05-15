def palindrome(s):
    # 큐를 정의
    queue = []
    # 스택을 정의
    stack = []

    refined_string = s.lower()

    for char in refined_string:
        queue.append(char)
        stack.append(char)

    n = len(s)

    for i in range(n):
        ele_q = queue.pop(0)
        ele_s = stack.pop()

        if ele_q !=ele_s:
            return False

    return True



print(palindrome("Wow"))
