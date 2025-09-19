from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        half = (m + n) // 2

        if m >= n:
            low = max(0, half-n)
            high = min(m, half)

            while high > low:
                i = (low + high) // 2
                j = half - i
                L1 = nums1[i-1]
                R1 = nums1[i]
                L2 = nums2[j-1]
                R2 = nums2[j]

                if L1 > R2: high =

        else:




if __name__ == "__main__":
    arr1 = [1,2]
    arr2 = [3,4]

    sol = Solution()

    result = sol.findMedianSortedArrays(arr1, arr2)
    print(result)