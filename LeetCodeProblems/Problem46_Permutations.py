from typing import List

class Solution:

    result = []

    def get_permutes(self, arr, freq, path):
        if len(path) == len(arr):
            self.result.append(path.copy())
            return

        for n in arr:
            if freq[n] > 0:
                path.append(n)
                freq[n] -= 1
                self.get_permutes(arr, freq, path)
                freq[path.pop()] += 1


    def get_freqs(self, nums):
        result = {}
        for n in nums:
            if n in result:
                result[n] += 1
            else:
                result[n] = 1

        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        freqs = self.get_freqs(nums)
        path = []
        self.get_permutes(nums, freqs, path)
        print(self.result)




if __name__ == "__main__":
    nums = [1,2,3]

    solution = Solution()

    answer = solution.permute(nums)

    print(answer)