class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


def some_test():
    a = Solution()
    input_board = ""
    target = "ABCDEFGHI"
    print(input_board)
    res = a.partition(input_board)
    print(f"is palindrome = {a.is_palindrome(input_board)}")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
