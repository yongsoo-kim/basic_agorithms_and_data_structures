def search_graph(graph, start):
    queue = []
    searched = set()

    # add start node
    queue.append(start)
    searched.add(start)

    while queue:
        q = queue.pop(0)
        print(q)
        for adjacent in graph[q]:
            if adjacent not in searched:
                queue.append(adjacent)
                searched.add(adjacent)


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [],
    4: [2],
    5: []
}

search_graph(graph, 1)
