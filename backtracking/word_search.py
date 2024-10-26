#link-https://leetcode.com/problems/word-search/description/

"""
Relationship Between DFS and Backtracking
In your case:

The DFS approach explores adjacent cells in the grid in a deep-first manner (going deep along a path of neighboring cells).
The Backtracking approach is the process of undoing moves (i.e., "backtracking" to a previous state) when a solution path turns out to be incorrect (i.e., the current sequence of characters does not form the word).
Often, DFS with backtracking is used together in these types of problems:

DFS is the search method used to explore each path.
Backtracking ensures that when a path doesn’t work, you undo (or "backtrack") to try other possible paths without repeating any incorrect decisions.
"""

def exist(board, word):
    def dfs(x, y, index):
        # If the entire word is found
        if index == len(word):
            return True
        # Boundary and validity check
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]:
            return False
        
        # Mark the cell as visited by temporarily changing its value
        temp = board[x][y]
        board[x][y] = "#"

        # Explore all 4 directions (up, down, left, right)
        found = (dfs(x + 1, y, index + 1) or
                 dfs(x - 1, y, index + 1) or
                 dfs(x, y + 1, index + 1) or
                 dfs(x, y - 1, index + 1))
        
        # Backtrack by restoring the original value of the cell
        board[x][y] = temp

        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
