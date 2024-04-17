import heapq
import math


class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        """
        You are given an m x n binary matrix grid.
         An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
        You may assume all four edges of the grid are surrounded by water.

        The area of an island is the number of cells with a value 1 in the island.

        Return the maximum area of an island in grid. If there is no island, return 0.
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        visited_loc = set()
        max_size = 0

        def dfs(grid, i, j, m, n, size):
            if i >= m or i < 0:
                return size
            if j >= n or j < 0:
                return size
            if grid[i][j] == 0:
                return size
            if (i, j) in visited_loc:
                return size
            visited_loc.add((i, j))
            size += 1
            size = dfs(grid, i - 1, j, m, n, size)
            size = dfs(grid, i + 1, j, m, n, size)
            size = dfs(grid, i, j - 1, m, n, size)
            size = dfs(grid, i, j + 1, m, n, size)
            return size

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited_loc.add((i, j))
                    continue
                if grid[i][j] == 1 and (i, j) not in visited_loc:
                    new_size = dfs(grid, i, j, m, n, 0)
                    if new_size > max_size:
                        max_size = new_size
        return max_size


def some_test():
    a = Solution()
    input_board = [[0,0,0,0,0,0,0,0]]
    target = 2
    print(input_board)
    res = a.maxAreaOfIsland(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
