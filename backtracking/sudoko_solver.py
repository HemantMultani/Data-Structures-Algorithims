"""
Problem link:
https://leetcode.com/problems/sudoku-solver/
"""

class Solution:
    def isValid(self, i, j, c, board):
        for k in range(9):
            #check in row
            if board[i][k]==c:
                return False
            #check in col
            if board[k][j]==c:
                return False
            #check in box
            if board[3*(i//3)+(k//3)][3*(j//3)+(k%3)]==c:
                return False
        return True
            
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for c in '123456789':
                        if self.isValid(i,j,c,board):
                            board[i][j]=c
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]='.'
                    return False
        return True
