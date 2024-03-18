class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid.
        Only the filled cells need to be validated according to the following rules:
            1)Each row must contain the digits 1-9 without repetition
            2)Each column must contain the digits 1-9 without repetition
            3)Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        NOTE:
            *)A Sudoku board (partially filled) could be valid but is not necessarily solvable
            *)Only the filled cells need to be validated according to the mentioned rules
        :param board:
        :return:
        """
        # So this case is again a counter for amount of times a number occurs in a set.
        # we can make helper functions that check the amount of times a number is placed in the board
        row_list = [[] for i in range(len(board))]
        # first run through all the columns
        for i in range(len(board[0])):
            col_res = self.is_1d_array_ok(board[i])
            if not col_res:
                return False
            for j in range(len(board[i])):
                row_list[j].append(board[i][j])

        # print("#################################")
        # Then run through all the rows
        for i in range(len(row_list)):
            row_res = self.is_1d_array_ok(row_list[i])
            if not row_res:
                return False

        # Lastly run through all 3X3 squares.
        for i in range(3, len(board) + 1, 3):
            for j in range(3, len(board[0]) + 1, 3):
                sub_matrix = [row[i - 3:i] for row in board[j - 3:j]]
                test = self.is_2d_array_ok(sub_matrix)
                if not test:
                    return False

        return True

    def is_1d_array_ok(self, array_1d: [str]) -> bool:
        """
        checks if a 1d array has any value that shows up more than once.
        every value except '.'
        :param array_1d:
        :return:
        """
        # print(array_1d)
        value_dict = {}
        for item in array_1d:
            if item not in value_dict:
                value_dict[item] = 1
            else:
                value_dict[item] += 1
                if item != '.':
                    return False
        return True

    def is_2d_array_ok(self, array_2d: [[str]]) -> bool:
        # print(array_2d)
        value_dict = {}

        for i in range(len(array_2d)):
            for j in range(len(array_2d[i])):
                item = array_2d[i][j]
                if item not in value_dict:
                    value_dict[item] = 1
                else:
                    value_dict[item] += 1
                    if item != '.':
                        return False
        return True


def some_test():
    a = Solution()
    input_board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(
        a.isValidSudoku(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
