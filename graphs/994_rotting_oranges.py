import heapq
import math


class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        """
        You are given an m x n grid where each cell can have one of three values:

            0 representing an empty cell,
            1 representing a fresh orange, or
            2 representing a rotten orange.

        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
        :param grid:
        :return:
        """
        visited = set()
        q = []
        m = len(grid)
        n = len(grid[0])
        rot_loc = []
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if grid[i][j] != 0:
                    q.append((i, j))
                    visited, rot = self.find_islands(grid, q, visited, m, n)
                    rot_loc.extend(rot)
                    if len(rot) == 0:
                        return -1
                visited.add((i, j))
        print(rot_loc)
        return self.time_to_rot(grid, rot_loc, m, n)

    def find_islands(self, grid: [[int]], q: [], visited: set, m: int, n: int):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rot_loc = []
        while q:
            x, y = q.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if grid[x][y] == 2:
                rot_loc.append((x, y))
            for (x_1, y_1) in directions:
                if x_1 + x >= m or x_1 + x < 0:
                    continue
                if y_1 + y >= n or y_1 + y < 0:
                    continue
                if grid[x_1 + x][y_1 + y] == 0:
                    continue
                q.append((x_1 + x, y_1 + y))
        return visited, rot_loc

    def time_to_rot(self, grid: [[int]], q: [], m, n):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = -1
        temp = []
        while q or temp:
            while q:
                x, y = q.pop()
                for (x_1, y_1) in directions:
                    if x_1 + x >= m or x_1 + x < 0:
                        continue
                    if y_1 + y >= n or y_1 + y < 0:
                        continue
                    if grid[x_1 + x][y_1 + y] == 0:
                        continue
                    if grid[x_1 + x][y_1 + y] == 1:
                        grid[x_1 + x][y_1 + y] = 2
                        temp.append((x_1 + x, y_1 + y))
            step += 1
            q = temp[::]
            temp = []
        return max(0,step)


def some_test():
    a = Solution()
    input_board = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    target = 2
    print(input_board)
    res = a.orangesRotting(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
