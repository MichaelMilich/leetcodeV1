class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i: int, word: str):
            if i >= len(digits):
                res.append(word)
                return
            let = letters[digits[i]]
            for j in range(len(let)):
                dfs(i + 1, word + let[j])

        dfs(0,"")
        return res


def some_test():
    a = Solution()
    input_board = "29"
    target = "ABCDEFGHI"
    print(input_board)
    res = a.letterCombinations(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
