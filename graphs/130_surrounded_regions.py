class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(i, j):
            nonlocal m
            nonlocal n
            visited.add((i, j))
            for x, y in directions:
                if i + x < 0 or j + y < 0:
                    continue
                if i + x >= m or j + y >= n:
                    continue
                if (i + x, j + y) in visited:
                    continue
                if board[i + x][j + y] == "O":
                    dfs(i + x, j + y)

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j)
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    board[i][j] = "X"


