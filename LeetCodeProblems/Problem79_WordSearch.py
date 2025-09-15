from typing import List

class Solution:
    def dfs(self, r, c, i, vis, board, word):
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]

        # bounds
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False

        # reuse
        if (r, c) in vis:
            return False

        # mismatch
        if board[r][c] != word[i]:
            return False

        # finished
        if i == len(word) - 1:
            return True


        vis.add((r,c))

        for dir in directions:
            nr = r + dir[0]
            nc = c + dir[1]

            if self.dfs(nr, nc, i+1, vis, board, word):
                return True


        vis.remove((r,c))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if self.dfs(r, c, 0, visited, board, word):
                        return True

        return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"

    solution = Solution()

    answer = solution.exist(board, word)

    print(answer)