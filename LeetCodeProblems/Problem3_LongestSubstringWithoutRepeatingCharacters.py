class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        temp = 0
        lens = len(s)

        for i in range(lens):
            used_char = {s[i]: 1}
            temp = 1
            for j in range(i+1, lens):
                if s[j] in used_char:
                    result = temp if temp > result else result
                    break
                else:
                    used_char[s[j]] = 1
                    temp += 1

            result = temp if temp > result else result

        return max(result, temp)


if __name__ == "__main__":
    test_string = "dvdf"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(test_string)

    print(result)