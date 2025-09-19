class Solution:
    def twoSum(self, nums, target):
        td = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n in td:
                return [td[n], i]
            else:
                td[diff] = i




if __name__ == "__main__":
    solution = Solution()

    nums = [2, 3, 3, 15]
    target = 6

    result = solution.twoSum(nums, target)

    print(result)