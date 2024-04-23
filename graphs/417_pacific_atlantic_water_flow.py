class Solution:
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                    (r, c) in visit
                    or r < 0
                    or c < 0
                    or r == ROWS
                    or c == COLS
                    or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c)) 
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


def some_test():
    a = Solution()
    input_board = [[2,1],[1,2]]
    target = 4
    print(input_board)
    res = a.pacificAtlantic(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
