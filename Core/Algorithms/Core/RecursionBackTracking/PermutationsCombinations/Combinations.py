def get_combinations(arr, k, path, start, result):
    if len(path) == k:
        result.append(path.copy())
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        get_combinations(arr, k, path, i + 1, result)
        path.pop()

if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 2
    result = []

    get_combinations(nums, k, [], 0, result)

    print(result)