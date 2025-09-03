def heapify(start, end, arr):
    last_non_leaf = (len(arr) // 2) - 1

    for i in range(last_non_leaf, -1, -1):
        left = i * 2 + 1
        right = i * 2  + 2

        if left < end + 1:
            if arr[left] > arr[i]:
                arr[left], arr[i] = arr[i], arr[left]
                heapify(start, end, arr)

        if right < end + 1:
            if arr[right] > arr[i]:
                arr[right], arr[i] = arr[i], arr[right]
                heapify(start, end, arr)


def heap_sort(start, end, arr):
    if start >= end:
        return

    heapify(start, end, arr)

    arr[0], arr[end] = arr[end], arr[0]

    heap_sort(start, end - 1, arr)


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(array)
    heap_sort(0, len(array) - 1, array)
    print(array)