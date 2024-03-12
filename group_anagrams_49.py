class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
        :param strs:
        :return:
        """
        return self.group_strings_same_length(strs)

    def group_strings_same_length(self, strings_same_length: [str]):
        # if there is only one string of the given length, it is an anagram of itself
        if len(strings_same_length) == 1:
            return [strings_same_length]

        dicts_list = {}
        for a_string in strings_same_length:
            string_dic = str(sorted(a_string))
            if string_dic not in dicts_list:
                dicts_list[string_dic] = [a_string]
            else:
                dicts_list[string_dic].append(a_string)
        print(f"dict values = {dicts_list.values()}")
        return list(dicts_list.values())



    def defining_charchters(self, a_string: str):
        """
        for any string calculates the amount of each char in it and returns a dict representing this
        :param a_string:
        :return:
        """
        abc = 'abcdefghijklmnopqrstuvwxyz'
        str_dict = {key: 0 for key in abc}

        for a_char in a_string:
            if a_char not in str_dict:
                str_dict[a_char] = 1
            else:
                str_dict[a_char] += 1
        s=""
        for b_char in str_dict:
            if str_dict[b_char] >0:
                s+=b_char*str_dict[b_char]
        return s


def some_test():
    a = Solution()
    print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
