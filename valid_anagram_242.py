class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once
        :param s:
        :param t:
        :return:
        """
        if len(t) != len(s):
            return False

        t_dict = {}
        s_dict = {}
        for i in range(len(t)):
            t_char = t[i]
            s_char = s[i]
            if t_char in t_dict:
                t_dict[t_char] += 1
            else:
                t_dict[t_char] = 1
            if s_char in s_dict:
                s_dict[s_char] += 1
            else:
                s_dict[s_char] = 1
        for c in s_dict:
            if c not in t_dict:
                return False
            if s_dict[c] != t_dict[c]:
                return False
        return True



def some_test():
    a = Solution()
    print(a.isAnagram("anagram", "nagaram"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
