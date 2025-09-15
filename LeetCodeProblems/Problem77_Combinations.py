class Solution:
    def get_combinations(self, arr, k, start, path, result):
        if len(path) == k:
            result.append(path.copy())

        for i in range(start, len(arr)):
            path.append(arr[i])
            self.get_combinations(arr, k, i + 1, path, result)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.get_combinations(range(1, n+1), k, 0, [], result)
        return result