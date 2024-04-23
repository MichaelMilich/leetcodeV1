class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            res, resLen = self.check(s, i, i, resLen, res)
            res, resLen = self.check(s, i, i + 1, resLen, res)
        return res

    def check(self, s, start_1, start_2, resLen, res):
        l, r = start_1, start_2
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
        return res, resLen


def some_test():
    a = Solution()
    input_case = "cbbd"
    print(input_case)
    res = a.longestPalindrome(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
