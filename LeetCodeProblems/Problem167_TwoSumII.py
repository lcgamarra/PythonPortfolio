from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1

        while True:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i, j]




if __name__ == "__main__":
    numbers = [2,7,11,15]
    solution = Solution()

    result = solution.twoSum(numbers, target=9)

    print(result)