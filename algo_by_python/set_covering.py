#Greedy알고리즘의 예.
# 방송하고자하는 주의 목록
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 선택된 방송국의 목록
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 방문할 방송국의 목록
final_stations = set()

# 방송하고자하는 주의 목록이 빌때까지 계속해서 처리
while states_needed:
    # 아직 방송이 되지 않는 주 중에서 가장 많은 주를 커버하고 있는 방송국을 고른다.
    best_station = None
    # 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
