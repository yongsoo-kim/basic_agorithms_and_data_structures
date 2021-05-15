# 3개의 딕셔너리가 필요.

# 노드와 이웃과 가중치
graph = dict()
# 최소비용 저장용
costs = dict()
# 부모 노드 저장용
parents = dict()

# 처리가 끝난 노드는 여기에 저장.
processed = []

graph = {
    "A": {
        "B": 2,
        "C": 5
    },
    "B": {
        "C": 8,
        "D": 7
    },
    "C": {
        "E": 4,
        "D": 2
    },
    "D": {
        "F": 1
    },
    "E": {
        "D": 6,
        "F": 3
    },
    "F": {}
}

infinity = float("inf")

costs["A"] = infinity
costs["B"] = infinity
costs["C"] = infinity
costs["D"] = infinity
costs["E"] = infinity
costs["F"] = infinity

parents["A"] = None
parents["B"] = None
parents["C"] = None
parents["D"] = None
parents["E"] = None
parents["F"] = None

start_node = "A"
end_node = "F"


def find_shortest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for c in costs.keys():
        if costs[c] < lowest_cost and c not in processed:
            lowest_cost = costs[c]
            lowest_cost_node = c

    return lowest_cost_node


def find_shortest_way(graph, start_node, end_node):
    # 초기 세팅
    init(graph, start_node)

    # 가장 비용이 싼 인접노드를 찾아라.
    target_node = find_shortest_cost_node(costs)

    while target_node is not None:
        cost = costs[target_node]
        neighbors = graph[target_node]
        for nk in neighbors.keys():
            new_cost = cost + neighbors[nk]
            if costs[nk] > new_cost:
                costs[nk] = new_cost
                parents[nk] = target_node

        processed.append(target_node)
        target_node = find_shortest_cost_node(costs)

    print_shortest_path(parents, end_node)


def init(graph, start_node):
    neighbor_nodes = graph[start_node]
    for n in neighbor_nodes.keys():
        # 스타트 노드주위의 인접 노드들에 대한 비용을 갱신
        costs[n] = neighbor_nodes[n]
        # 인접 노드들의 부모노드를 스타드노드로 갱신.
        parents[n] = start_node


def print_shortest_path(parents, end_node):
    path = []
    path.append(end_node)
    parent = parents[end_node]

    while parent is not None:
        path.append(parent)
        parent = parents[parent]

    path.reverse()
    print(path)


if __name__ == "__main__":
    find_shortest_way(graph, "A", "F")
