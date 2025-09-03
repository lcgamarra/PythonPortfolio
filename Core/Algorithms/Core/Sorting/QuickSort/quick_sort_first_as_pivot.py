def quick_sort(start, end, arr):
    if start >= end:
        return

    pivot = arr[start]

    i = end + 1
    for j in range(end, start, -1):
        if arr[j] > pivot:
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i-1], arr[start] = arr[start], arr[i-1]

    quick_sort(start, i-2, arr)
    quick_sort(i, end, arr)


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(array)
    quick_sort(0, len(array) - 1, array)
    print(array)