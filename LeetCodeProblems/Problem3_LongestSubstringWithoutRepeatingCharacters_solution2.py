class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        lens = len(s)
        i = 0
        visited = {}

        for j in range(lens):
            if s[j] not in visited:
                result = max(j - i + 1, result)
                visited[s[j]] = 0
            else:
                while s[j] in visited:
                    visited.pop(s[i])
                    i += 1
                visited[s[j]] = 0

        return result


if __name__ == "__main__":
    test_string = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(test_string)

    print(result)