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


def find_way_in_maze(graph, start, end):
    queue = []
    searched = set()
    possible_paths = []

    queue.append([start])

    while queue:
        q = queue.pop(0)
        last_node = q[-1]
        searched.add(last_node)
        if last_node is end:
            possible_paths.append(q)
        else:
            for neighbor_node in graph[last_node]:
                if neighbor_node not in searched:
                    new_path = q.copy()
                    new_path.append(neighbor_node)

                    queue.append(new_path)

    find_shortest_path(possible_paths)


def find_shortest_path(paths):
    n = len(paths)
    min_len = 0
    min_idx = 0
    for i in range(n):
        if len(paths[i]) < min_len:
            min_len = len(paths[i])
            min_idx = i

    print(paths[min_idx])

    # Keep doing while queue is not empty
    # pop a node from left
    # print popped node.
    # if popped node is end node, end the process
    # find neighbor nodes from popped node.
    # if neighbor node is not searched yet
    # add queue and searched set


find_way_in_maze(maze, 'a', 'p')
