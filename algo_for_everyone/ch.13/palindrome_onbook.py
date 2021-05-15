def palindrome(s):
    # 큐를 정의
    # 참고로, 리스트로 정의하는 큐는 비효율적이다(pop할때마다 다른 요소들을 앞으로 하나씩 당겨줘야하기 때문.)
    # 그러므로 왠만하면 deque를 import 해서 사용하자.
    qu = []
    # 스택을 정의
    st = []

    for x in s:
        # 해당문자가 알파벳이면(공백, 숫자 특수 문자가 아니면)
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
