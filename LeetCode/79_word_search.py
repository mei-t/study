from typing import List

# m = len(board)
# n = len(board[0])
# TC: O(m * n * 3 ^ l)
# SC: O(max(m * n, l))
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False] * len(board[0]) for i in range(len(board))]
                    if self.search(board, word, 0, i, j, visited):
                        return True
        
        return False
    
    def search(self, board: List[List[str]], word: str, l: int, i: int, j: int, visited:List[List[bool]]) -> bool:
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[l]:
            return False
        if l + 1 == len(word):
            return True
        visited[i][j] = True
        if self.search(board, word, l + 1, i - 1, j, visited):
            return True
        if self.search(board, word, l + 1, i, j - 1, visited):
            return True
        if self.search(board, word, l + 1, i + 1, j, visited):
            return True
        if self.search(board, word, l + 1, i, j + 1, visited):
            return True
        visited[i][j] = False
        return False

# m = len(board)
# n = len(board[0])
# l = len(word)
# TC: O(m * n * 3 ^ l)
# SC: O(l)
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.search(word, i, j):
                    return True
        
        return False
    
    def search(self, suffix: str, row: int, col: int) -> bool:
        if len(suffix) == 0:
            return True
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS or self.board[row][col] != suffix[0]:
            return False
        self.board[row][col] = '#'
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            res = self.search(suffix[1:], row + rowOffset, col + colOffset)
            if res: break
        self.board[row][col] = suffix[0]
        return res

if __name__ == '__main__':
    sol = Solution2()
    # print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(sol.exist(
        [
            ["A","A","A","A","A","A"],
            ["A","A","A","A","A","A"],
            ["A","A","A","A","A","A"],
            ["A","A","A","A","A","A"],
            ["A","A","A","A","A","A"],
            ["A","A","A","A","A","A"]
        ],
        "AAAAAAAAAAAABAA"))