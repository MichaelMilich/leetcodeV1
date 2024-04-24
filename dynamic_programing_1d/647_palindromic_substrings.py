class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Given a string s, return the number of palindromic substrings in it.

        A string is a palindrome when it reads the same backward as forward.

        A substring is a contiguous sequence of characters within the string.
        :param s:
        :return:
        """
        count=0
        for i in range(len(s)):
            count += self.check(s, i, i)
            count += self.check(s, i, i+1)
        return count

    def check(self, s, start_1, start_2):
        l, r = start_1, start_2
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

def some_test():
    a = Solution()
    input_case = "cbbd"
    print(input_case)
    res = a.countSubstrings(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()