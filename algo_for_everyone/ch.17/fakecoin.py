def weigh(a, b, c, d):
    fake = 29  # 가짜 동전의 위치.
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


def find_fakecoin(left, right):
    # 종료조건: 가짜 동전이 있을 범위안에 동전이 한개뿐이면 그 동전이 가까 동전임.
    if left == right:
        return left

    # left에서 right까지 놓인 동전을 두 그룹으(g1_left~g1_right, g2_left~g2_right)로 나눔
    # 동전수가 홀수면 두그룹으로 나누고 마지막에 있는 동전(right) 가 한개 남음.
    half = (right - left + 1) // 2

    g1_left = left
    g1_right = left + half - 1

    g2_left = left + half
    g2_right = g2_left + half - 1

    # 나눠진 두 그룹을 weigh()함수를 이용하여 저울질 함.
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == -1:  # 그룹1 이 가벼움(가짜 동전이 이 그룹에 있음)
        # 그룹1 범위를 재귀 호출로 다시 조사
        return find_fakecoin(g1_left, g1_right)
    elif result == 1:  # 그룹2 가 가벼움(가짜 동전이 이 그룹에 있음)
        return find_fakecoin(g2_left, g2_right)
    else:  # 두 그룹의 무게가 같으면(나뉜 두 그룹안에 가짜 동전이 없다면)
        return right


n = 100

print(find_fakecoin(0, n - 1))
print(find_fakecoin(1, n))
