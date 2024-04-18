class Solution:
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        grid = [["" for _ in x] for x in heights]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []
        visited = set()

        def dfs(i: int, j: int, m: int, n: int):
            if (i, j) in visited:
                return grid[i][j]
            visited.add((i,j))
            for (x, y) in directions:
                if i - x < 0 or j - y < 0:
                    grid[i][j] += "P"
                if i+x >=m or j+y >=n:
                    grid[i][j] += "A"
                if len(grid[i][j]) >= 2:
                    res.append([i,j])

            print("hi")

        return res
