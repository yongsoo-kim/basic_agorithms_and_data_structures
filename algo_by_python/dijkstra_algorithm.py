graph = {
    "START": {
        "A": 6,
        "B": 2
    },
    "A": {
        "FIN": 1
    },
    "B": {
        "A": 3,
        "FIN": 5
    },
    "FIN": {}
}

infinity = float("inf")
costs = {}
costs["A"] = 6
costs["B"] = 2
costs["FIN"] = infinity

parents = {}
parents["A"] = "START"
parents["B"] = "START"
parents["FIN"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)



print(parents)
