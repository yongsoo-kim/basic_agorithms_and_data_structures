maze = {
    'a': ['e'],
    'e': ['a', 'i'],
    'i': ['e', 'm'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'j': ['n', 'f', 'k'],
    'k': ['j', 'o'],
    'o': ['k'],
    'f': ['j', 'b', 'g'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'l': ['h', 'p'],
    'p': ['l']
}


def solve_maze(g, start, end):
    qu = []  # 기억장소 1: 앞으로 처리해야할 이동 경로를 큐에 저장
    done = set()  # 기억장소2: 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)

    qu.append(start)
    done.add(start)

    while qu:  # 큐에 처리할 경로가 남아있으면
        p = qu.pop(0)  # 큐에서 처리 대상을 꺼냄
        v = p[-1]  # 큐에서 저장된 경로의 마지막 문자가 현재 처리해야 할 꼭지점.
        if v == end:  # 처리해야 할 꼭짓점이 도착점이면(목적지 도착!)
            return p  # 지금까지의 전체 이동 경로를 돌려주고 종료.
        for x in g[v]:  # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done:  # 아직 큐에 추가된적이 없는 꼭짓점을
                qu.append(p + x)  # 이동경로에 새 꼭짓점으로 추가하여 큐에 저장하고
                done.add(x)  # 집합에도 추가.

    # 탐색을 마릴땍까지 도착점이 나오지 않으면 나갈수 없는 미로임
    return "?"


print(solve_maze(maze, 'a', 'p'))
