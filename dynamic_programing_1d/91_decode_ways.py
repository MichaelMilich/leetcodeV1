class Solution:
    def numDecodings(self, s: str) -> int:
        """
        A message containing letters from A-Z can be encoded into numbers using the following mapping:
            'A' -> "1"
            'B' -> "2"
            ...
            'Z' -> "26"

        To decode an encoded message,
        all the digits must be grouped then mapped back into letters using the reverse of the mapping above
        (there may be multiple ways).

        For example, "11106" can be mapped into:
            "AAJF" with the grouping (1 1 10 6)
            "KJF" with the grouping (11 10 6)
        Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F'
        since "6" is different from "06".

        Given a string s containing only digits, return the number of ways to decode it.
        The test cases are generated so that the answer fits in a 32-bit integer.

        :param s:
        :return:
        """
        decode_dict = {
            '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
            '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S',
            '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'
        }
        arr = [0] * (len(s)+1)
        arr[-1] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                arr[i] = 0
            else:
                arr[i] = arr[i + 1]
                temp = s[i:i+2]
                if i + 1 < len(s) and int(s[i:i+2])<=26:
                    arr[i] += arr[i + 2]
        return arr[0]


def some_test():
    a = Solution()
    input_case = "06"
    print(input_case)
    res = a.numDecodings(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
