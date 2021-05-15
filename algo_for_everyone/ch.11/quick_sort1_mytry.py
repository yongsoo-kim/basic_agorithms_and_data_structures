def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]

    # list of smaller than pivot
    smaller = [i for i in a[1:] if i < pivot]

    # list of larger than pivot
    larger = [j for j in a[1:] if j > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))
