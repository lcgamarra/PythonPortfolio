def heapify(start, end, arr):
    if start >= end:
        return

    shift = start

    last_non_leaf_index = ((end - start + 1) // 2) - 1

    for i in range(last_non_leaf_index, -1, -1):

        if (2*i + 1) + shift < len(arr):
            if arr[2*i + 1 + shift] < arr[i + shift]:
                arr[2*i + 1 + shift], arr[i + shift] = arr[i + shift], arr[2*i + 1 + shift]
                heapify(start, end, arr)

        if (2*i + 2) + shift < len(arr):
            if arr[2*i + 2 + shift] < arr[i + shift]:
                arr[2*i + 2 + shift], arr[i + shift] = arr[i + shift], arr[2*i + 2 + shift]
                heapify(start, end, arr)

def min_heap_sort(start, end, arr):
    if start >= end:
        return

    heapify(start, end, arr)

    min_heap_sort(start+1, end, arr)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(array)
    min_heap_sort(0, len(array) - 1, array)
    print(array)