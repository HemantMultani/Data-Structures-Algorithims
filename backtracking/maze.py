"""
Problem link:
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
"""

from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        visited[entrance[0]][entrance[1]] = 1
        while q:
            r,c,steps = q.popleft()
            for dr,dc in [(-1,0), (0,-1), (1,0), (0,1)]:
                if -1<r+dr<m and -1<c+dc<n and maze[r+dr][c+dc]=='.' and visited[r+dr][c+dc]==0:
                    row, col = r+dr, c+dc
                    if (row==0 or row==m-1 or col==0 or col==n-1) and [row,col]!=entrance: return steps+1
                    q.append((row, col, steps+1))
                    visited[row][col] = 1
        return -1
