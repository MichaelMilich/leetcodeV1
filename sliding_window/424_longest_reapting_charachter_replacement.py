class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        todo: do this again, I didn't do it alone
        You are given a string s and an integer k.
        You can choose any character of the string and change it to any other uppercase English character.
        You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get
        after performing the above operations.
        :param s:
        :param k:
        :return:
        """
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


def some_test():
    a = Solution()
    input_board = "AABABBA"
    target = 1
    print(input_board)
    res = a.characterReplacement(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
