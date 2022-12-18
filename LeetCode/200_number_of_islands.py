from typing import List

# m * n grid
# TC: O(m * n)
# SC: O(m * n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        self.visited = [[0] * self.col for i in range(self.row)]
        res = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == '1' and not self.visited[i][j]:
                    self.checkWholeIsland(i, j)
                    res += 1

        return res
    
    def checkWholeIsland(self, r: int, c: int) -> None:
        if r < 0 or r >= self.row or c < 0 or c >= self.col:
            return
        if self.grid[r][c] == '0' or self.visited[r][c]:
            return
        
        self.visited[r][c] = 1
        self.checkWholeIsland(r - 1, c)
        self.checkWholeIsland(r, c - 1)
        self.checkWholeIsland(r + 1, c)
        self.checkWholeIsland(r, c + 1)


# m * n grid
# TC: O(m * n)
# SC: O(1))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        res = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == '1':
                    self.checkWholeIsland(i, j)
                    res += 1

        return res
    
    def checkWholeIsland(self, r: int, c: int) -> None:
        if r < 0 or r >= self.row or c < 0 or c >= self.col:
            return
        if self.grid[r][c] == '0':
            return
        
        self.grid[r][c] = '0'
        self.checkWholeIsland(r - 1, c)
        self.checkWholeIsland(r, c - 1)
        self.checkWholeIsland(r + 1, c)
        self.checkWholeIsland(r, c + 1)
