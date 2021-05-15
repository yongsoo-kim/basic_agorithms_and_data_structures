def print_all_friends(fr_info, target_name):
    qu = []
    done = set()

    qu.append(target_name)  # 자신을 큐에 넣고 시작
    done.add(target_name)  # 집합에도 추가

    while qu:  # 큐에 처리할 사람이 남아있는 동안
        p = qu.pop(0)  # 큐에서 처리 대상을 한명 꺼내
        # print(p) # 이름을 출력하고
        for x in fr_info[p]:  # 그의 친구들 중에
            if x not in done:  # 아직 큐에 추가 된 적이 없는 사람을
                qu.append(x)  # 큐에 추가하고
                done.add(x)  # 집합에도 추가.

    print(done)


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
