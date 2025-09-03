def merge_arrays(m, n):
    i = 0
    j = 0
    result = []

    while i < len(m) and j < len(n):
        if m[i] < n[j]:
            result.append(m[i])
            i += 1
        else:
            result.append(n[j])
            j += 1

    result.extend(m[i:])
    result.extend(n[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge_arrays(left, right)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(array)
    sorted_array = merge_sort(array)
    print(sorted_array)