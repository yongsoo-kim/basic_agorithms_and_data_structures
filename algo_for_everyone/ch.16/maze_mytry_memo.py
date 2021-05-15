maze = {
    'a': ['d', 'b'],
    'b': ['a', 'c'],
    'c': ['b'],
    'd': ['a']
}


def find_way_in_maze(graph, start, end):
    queue = []
    searched = set()

    queue.append([start])

    while queue:
        q = queue.pop(0)
        last_node = q[-1]
        searched.add(last_node)
        if last_node is not end:
            for neighbor_node in graph[last_node]:
                if neighbor_node not in searched:
                    new_path = q.copy()
                    new_path.append(neighbor_node)

                    queue.append(new_path)
        else:
            print(q)

            # Keep doing while queue is not empty
    # pop a node from left
    # print popped node.
    # if popped node is end node, end the process
    # find neighbor nodes from popped node.
    # if neighbor node is not searched yet
    # add queue and searched set


find_way_in_maze(maze, 'a', 'c')
