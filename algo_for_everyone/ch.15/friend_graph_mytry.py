def print_all_friends(fr_info, target_name):
    queue = []
    searched = []

    searched.append(target_name)
    queue.append(target_name)

    while queue:
        next_f = queue.pop(0)
        friends = fr_info.get(next_f)
        for f in friends:
            if f not in searched:
                queue.append(f)
                searched.append(f)

    print(searched)


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
