class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        An input string is valid if:
            *) Open brackets must be closed by the same type of brackets.
            *) Open brackets must be closed in the correct order.
            *) Every close bracket has a corresponding open bracket of the same type.
        :param s: the string
        :return: True if the string is vaild, false otherwise
        """
        open_bracket = {"{": "}", "[": "]", "(": ")"}
        close_bracket = {"}": "{", "]": "[", ")": "("}
        stack = []
        for num, c in enumerate(s):
            # print(f"index {num} = {c}")
            # print(f" stack = {stack}")
            if c in open_bracket:
                stack.append(c)
            if c in close_bracket:
                if close_bracket[c] not in stack:
                    return False
                if stack[-1] != close_bracket[c]:
                    return False
                stack.pop()
        # print(f"final stack = {stack}")
        return len(stack) == 0


def some_test():
    a = Solution()
    input_board = "[[({}){}]]"
    print(
        a.isValid(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
