class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
        In other words, return true if one of s1's permutations is the substring of s2.
        :param s1:
        :param s2:
        :return:
        """
        n2 = len(s2)
        n1 = len(s1)
        if n2 < n1:
            return False
        if n2 == 1:
            return s1 == s2

        s1_dict = dict()
        for c1 in s1:
            s1_dict[c1] = 1 + s1_dict.get(c1, 0)

        left, right = 0, 1
        s2_sub_dict = {s2[left]: 1}
        while right < n1-1:
            s2_sub_dict[s2[right]] = 1 + s2_sub_dict.get(s2[right], 0)
            right += 1

        while right < n2:
            if right-left != n1:
                s2_sub_dict[s2[right]] = 1 + s2_sub_dict.get(s2[right], 0)
                right += 1
            if s2_sub_dict == s1_dict:
                return True
            s2_sub_dict[s2[left]] -= 1
            if s2_sub_dict[s2[left]] == 0:
                s2_sub_dict.pop(s2[left])
            left+=1

        return s2_sub_dict == s1_dict

def some_test():
    a = Solution()
    input_board = "ab"
    target = "a"
    print(input_board)
    res = a.checkInclusion(target, input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
