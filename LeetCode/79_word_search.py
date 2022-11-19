from typing import List

class Solution:
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

if __name__ == '__main__':
    sol = Solution()
    # print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))