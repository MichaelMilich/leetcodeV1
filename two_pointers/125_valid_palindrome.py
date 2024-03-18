class Solution:
    def isPalindrome(self, s: str) -> bool:
        abcde = "0123456789abcdefghijklmnopqrstuvwxyz"
        new_s = ""
        for c in s:
            if c.lower() in abcde:
                new_s += c.lower()
        print(new_s)
        i = 0
        j = len(new_s) - 1
        while j >= i:
            if new_s[j] != new_s[i]:
                print(f"{new_s[j]}!={new_s[i]}")
                return False
            j-=1
            i+=1
        return True


def some_test():
    a = Solution()
    input_board = "0P"
    print(
        a.isPalindrome(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
