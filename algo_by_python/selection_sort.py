# Return the smallest element index from array
def find_smallest_index(array):
    smallest_index = 0
    smallest = array[0]
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            smallest_index = i
    return smallest_index


# Selection sort
def selection_sort(array):
    new_arr = []
    for i in range(len(array)):
        smallest_index = find_smallest_index(array)
        new_arr.append(array.pop(smallest_index))
    return new_arr


if __name__ == "__main__":
    my_array = [6, 7, 2, 4, 8, 1, 9, 5]

    print(selection_sort(my_array))
