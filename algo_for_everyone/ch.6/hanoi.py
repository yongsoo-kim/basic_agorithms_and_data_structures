def hanoi(n, from_pos, to_pos, support_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    # n-1개의 원반을 시작 기둥에서 보조 기둥으로 이동.(목표기둥은 보조기둥화)
    hanoi(n - 1, from_pos, support_pos, to_pos)

    # 제일 큰 원반을 시작기둥에서  목표 기둥으로 이동.
    print(from_pos, "->", to_pos)

    # n-1개의  보조 기둥의 원반을 목표 기둥으로 이동.(시작 기둥은 보조 기둥화)
    hanoi(n - 1, support_pos, to_pos, from_pos)

#hanoi(1, 1, 3, 2)
hanoi(2, 1, 3, 2)
#hanoi(3, 1, 3, 2)
