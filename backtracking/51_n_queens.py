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
        board = [["." for x in range(n)] for x in range(n)]
        available_space = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                available_space.add((i, j))

        def dfs(k: int, board: [[str]], available_space: set):
            if k == n:
                for i in range(len(board)):
                    board[i] = "".join(board[i])
                res.append(board)
                return
            if len(available_space) == 0:
                return
            for i in range(n):
                for j in range(n):
                    available_space_copy = available_space.copy()
                    board_copy = copy.deepcopy(board)
                    if (i, j) in available_space_copy:
                        board_copy[i][j] = "Q"
                        for ki in range(n):
                            if (ki, j) in available_space_copy:
                                available_space_copy.remove((ki, j))
                        for kj in range(n):
                            if (i, kj) in available_space_copy:
                                available_space_copy.remove((i, kj))
                        ki = i - 1
                        kj = j - 1
                        while ki >= 0 and kj >= 0:
                            if (ki, kj) in available_space_copy:
                                available_space_copy.remove((ki, kj))
                            ki -= 1
                            kj -= 1
                        ki = i - 1
                        kj = j + 1
                        while ki >= 0 and kj < n:
                            if (ki, kj) in available_space_copy:
                                available_space_copy.remove((ki, kj))
                            ki -= 1
                            kj += 1
                        ki = i + 1
                        kj = j + 1
                        while ki < n and kj < n:
                            if (ki, kj) in available_space_copy:
                                available_space_copy.remove((ki, kj))
                            ki += 1
                            kj += 1
                        ki = i + 1
                        kj = j - 1
                        while ki < n and kj >= 0:
                            if (ki, kj) in available_space_copy:
                                available_space_copy.remove((ki, kj))
                            ki += 1
                            kj -= 1
                        dfs(k + 1, board_copy, available_space_copy)

        dfs(0, board, available_space)
        return res


def some_test():
    a = Solution()
    input_board = 4
    target = "ABCDEFGHI"
    print(input_board)
    res = a.solveNQueens(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
