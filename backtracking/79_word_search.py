class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    path_set = set()
                    path_set.add((i,j))
                    result = self.search_word(board,word,1,path_set,i,j)
                    if result:
                        return True
        return False

    def search_word(self, board: [[str]], word: str, idx: int, path_set: set, i: int, j: int):
        """
        assumes that the call happened from the first letter
        :param board:
        :param word:
        :param idx:
        :param path_set:
        :param i:
        :param j:
        :return:
        """
        if idx >= len(word):
            return True
        if i + 1 < len(board):
            if board[i + 1][j] == word[idx] and (i + 1, j) not in path_set:
                path_set.add((i + 1, j))
                res = self.search_word(board, word, idx + 1, path_set, i + 1, j)
                path_set.remove((i + 1, j))
                if res:
                    return True
        if i - 1 >= 0:
            if board[i - 1][j] == word[idx] and (i - 1, j) not in path_set:
                path_set.add((i - 1, j))
                res = self.search_word(board, word, idx + 1, path_set, i - 1, j)
                path_set.remove((i - 1, j))
                if res:
                    return True
        if j + 1 < len(board[i]):
            if board[i][j + 1] == word[idx] and (i, j + 1) not in path_set:
                path_set.add((i, j + 1))
                res = self.search_word(board, word, idx + 1, path_set, i, j + 1)
                path_set.remove((i, j + 1))
                if res:
                    return True
        if j - 1 >= 0:
            if board[i][j - 1] == word[idx] and (i, j - 1) not in path_set:
                path_set.add((i, j - 1))
                res = self.search_word(board, word, idx + 1, path_set, i, j - 1)
                path_set.remove((i, j - 1))
                if res:
                    return True
        return False


def some_test():
    a = Solution()
    input_board = [["A","B","C"],["H","G","D"],["I","F","E"]]
    target = "ABCDEFGHI"
    print(input_board)
    res = a.exist(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
