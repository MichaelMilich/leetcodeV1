import copy


class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        """
        The n-queens puzzle:
          the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
        Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order
        Each solution contains a distinct board configuration of the n-queens' placement
        where 'Q' and '.' both indicate a queen and an empty space, respectively.
        :param n:
        :return:
        """
        res = []
        board = ["." * n for _ in range(n)]
        columns = {i: False for i in range(n)}
        rows = {i: False for i in range(n)}
        down_side = {i: False for i in range(-(n - 1), n)}
        up_side = {i: False for i in range(2 * (n - 1) + 1)}

        def dfs(i: int, n: int):
            if i >= n:
                res.append(board[:])
                return
            for j in range(n):
                check = not rows[j] and not columns[i] and not down_side[i-j] and not up_side[i+j]
                if check:
                    rows[j]=True
                    columns[i]=True
                    down_side[i-j]=True
                    up_side[i+j]=True
                    board[i]="."*j+"Q"+"."*(n-1-j)
                    dfs(i+1,n)
                    rows[j] = False
                    columns[i] = False
                    down_side[i - j] = False
                    up_side[i + j] = False
                    board[i] = "." * n
            return

        dfs(0,n)
        return res



def some_test():
    a = Solution()
    input_board = 5
    target = "ABCDEFGHI"
    print(input_board)
    res = a.solveNQueens(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
