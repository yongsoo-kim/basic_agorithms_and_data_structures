from collections import deque

graph = {}
graph["CAB"] = ["CAT", "CAR"]
graph["CAT"] = ["MAT", "BAT"]
graph["CAR"] = ["CAT", "BAR"]
graph["MAT"] = ["BAT"]
graph["BAR"] = ["BAT"]


def check_end_point(node):
    return node == "BAT"


def breadth_first_search2(name):
    search_queue = deque()
    search_queue += graph
    searched = []
    path={}

    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            print("now at '{target}'".format(target=node))
            if check_end_point(node):
                print("We did it!")
                return True
            else:
                search_queue += graph[node]
                searched.append(node)
    return False


if __name__ == "__main__":
    breadth_first_search2("CAB")
