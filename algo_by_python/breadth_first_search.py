from collections import deque

# 그래프 제공
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    # 바보같지만, 이름이 m으로 끝나는 사람을 찾자.(thom)
    return name[-1] == 'm'


def breadth_first_search(name):
    # 양방향 큐를 생성
    search_queue = deque()
    search_queue += graph[name]
    # 그래프가 무한순환하지 않게, 이미 검색한 사람은 이곳에 저장해 둔다.
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print("asking to '{target}'".format(target=person))
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return None


if __name__ == "__main__":
    breadth_first_search("you")
