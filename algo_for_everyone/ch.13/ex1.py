# 스택과 큐를 이용하지 않고 푸는 회문문제.

def palindrome(s):
    refined_string = []

    for char in s:
        if char.isalpha():
            refined_string.append(char.lower())

    n = len(refined_string)

    mid = n // 2

    for i in range(mid):
        if refined_string[i] != refined_string[n - 1 - i]:
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
