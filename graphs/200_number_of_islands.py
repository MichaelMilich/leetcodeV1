import heapq
import math


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
        return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        visited_loc = set()
        island_num = 0

        def dfs(grid, i, j, m, n):
            if i >= m or i < 0:
                return
            if j >= n or j < 0:
                return
            if grid[i][j] == "0":
                return
            if (i, j) in visited_loc:
                return
            visited_loc.add((i, j))
            dfs(grid, i - 1, j, m, n)
            dfs(grid, i + 1, j, m, n)
            dfs(grid, i, j - 1, m, n)
            dfs(grid, i, j + 1, m, n)
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    visited_loc.add((i, j))
                    continue
                if grid[i][j] == "1" and (i, j) not in visited_loc:
                    dfs(grid, i, j, m, n)
                    island_num += 1
        return island_num


def some_test():
    a = Solution()
    input_board = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    target = 2
    print(input_board)
    res = a.numIslands(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
