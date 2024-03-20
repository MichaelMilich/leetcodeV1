class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring
        without repeating characters.
        :param s:
        :return:
        """
        n = len(s)
        if n <= 1:
            return n
        left, right = 0, 1
        char_set = set(s[left])
        max_len = 1
        while right < n:
            temp = s[right]
            if s[right] in char_set:
                if max_len < len(char_set):
                    max_len = len(char_set)
                char_set.remove(s[left])
                left += 1
            else:
                char_set.add(s[right])
                right += 1
        if max_len < len(char_set):
            max_len = len(char_set)

        return max_len


def some_test():
    a = Solution()
    input_board = "abcabcbb"
    target = 823855818
    print(input_board)
    res = a.lengthOfLongestSubstring(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
