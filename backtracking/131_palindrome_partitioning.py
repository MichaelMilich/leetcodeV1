class Solution:
    def partition(self, s: str) -> [[str]]:
        """
        Given a string s, partition s such that every substring of the partition is a palindrome .
        Return all possible palindrome partitioning of s.
        :param s:
        :return:
        """
        n = len(s)
        res = []
        part = []

        def dfs(i: int):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
            return

        dfs(0)
        return res

    def isPalindrome(self, s: str):
        if len(s) == 0:
            return False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


def some_test():
    a = Solution()
    input_board = "ddadd"
    target = "ABCDEFGHI"
    print(input_board)
    res = a.partition(input_board)
    print(f"is palindrome = {a.partition(input_board)}")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
