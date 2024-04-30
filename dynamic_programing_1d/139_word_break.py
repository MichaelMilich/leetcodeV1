class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        """
        Given a string s and a dictionary of strings wordDict,
        return true if s can be segmented into a space-separated sequence of one or more dictionary words.

        Note that the same word in the dictionary may be reused multiple times in the segmentation.
        :param s:
        :param wordDict:
        :return:
        """
        s_len = len(s)
        if s_len == 0:
            return True
        q = []
        next_level = []
        level_counter = 0
        word_set = set()
        for word in wordDict:
            n = len(word)
            if word == s[:n]:
                q.append(word)
            if word == s:
                return True
        while q or next_level:
            while q:
                element = q.pop()
                for word in wordDict:
                    n = len(element + word)
                    if element + word == s:
                        return True
                    if element + word not in word_set and element + word == s[:n]:
                        word_set.add(element + word)
                        next_level.append(element + word)
            level_counter += 1
            q = next_level[:]
            next_level = []
        return False


def some_test():
    a = Solution()
    input_case = ["a","abc","b","cd"]
    target = "abcd"
    print(input_case)
    res = a.wordBreak(target,input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()

