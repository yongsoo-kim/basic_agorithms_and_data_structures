def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i < pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    my_list = [2, 5, 7, 9, 4, 1, 0, 8, 3]
    print(quick_sort(my_list))
