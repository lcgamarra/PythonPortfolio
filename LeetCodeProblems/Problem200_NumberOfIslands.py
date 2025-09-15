from collections import deque
from typing import List


class Solution:
    visited = set()

    def bfs(self, row, col, rows, cols, grid):
        queue = deque([(row, col)])
        self.visited.add((row, col))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            node = queue.popleft()

            row = node[0]
            col = node[1]

            for dir in directions:
                nr = row + dir[0]
                nc = col + dir[1]
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in self.visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        self.visited.add((nr, nc))


    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        if not grid or not grid[0]:
            return 0

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.bfs(row, col, rows, cols, grid)
                    count += 1

        return count

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    solution = Solution()

    print(solution.numIslands(grid))