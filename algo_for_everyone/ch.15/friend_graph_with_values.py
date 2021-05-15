def print_all_friends(fr_info, target_name):
    queue = []
    done = set()

    queue.append((target_name, 0))
    done.add(target_name)

    while queue:  # 큐가 남아있을동안
        (p, d) = queue.pop(0)  # 큐 좌측에서 한명을 꺼내
        print(p, d)  # 출력하고
        for f in fr_info[p]:  # 그 친구들중에
            if f not in done:  # 아직 검색이 끝나지 않은 친구들만
                queue.append((f, d + 1))  # 큐에 저장한다. 이때 친밀도를 1 증가시키고
                done.add(f)     # 집합에도 추가




fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')
