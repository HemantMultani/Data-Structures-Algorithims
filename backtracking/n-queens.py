"""
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/submissions/1439804041/
"""

class Solution:
    #dfs
    def placeQ(self, col, n, board, ans, nwd, wr, swd):
        if col==n:
            ans.append(board[:])
            return
        for row in range(n):
            if nwd[n-1 + col-row]==0 and wr[row]==0 and swd[row+col]==0:
                board[row] = board[row][:col]+'Q'+board[row][col+1:]
                nwd[n-1 + col-row] = 1
                wr[row] = 1
                swd[row+col] = 1
                self.placeQ(col+1, n, board, ans, nwd, wr, swd)

                #backtracking
                board[row] = board[row][:col]+'.'+board[row][col+1:]
                nwd[n-1 + col-row] = 0
                wr[row] = 0
                swd[row+col] = 0
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        nwd = [0 for _ in range(2*n-1)]
        wr = [0 for _ in range(n)]
        swd = [0 for _ in range(2*n-1)]
        board = ['.'*n for _ in range(n)]
        self.placeQ(0,n,board,ans,nwd,wr,swd)
        return ans
