def quick_sort(start_index, end_index, arr):
    if start_index >= end_index:
        return

    pivot = arr[end_index]

    i = start_index - 1
    for j in range(start_index, end_index + 1, 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end_index] = arr[end_index], arr[i+1]

    quick_sort(start_index, i, arr)
    quick_sort(i + 2, end_index, arr)


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(array)
    quick_sort(0, len(array) - 1, array)
    print(array)