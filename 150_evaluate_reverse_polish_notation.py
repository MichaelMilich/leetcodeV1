class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        """
        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
        Evaluate the expression. Return an integer that represents the value of the expression.
        Note that:
            *) The valid operators are '+', '-', '*', and '/'.
            *) Each operand may be an integer or another expression
            *) The division between two integers always truncates toward zero.
            *) There will not be any division by zero.
            *)The input represents a valid arithmetic expression in a reverse polish notation.
            *) The answer and all the intermediate calculations can be represented in a 32-bit integer.
        :param tokens:
        :return:
        """
        # so first we want to create a basic dict to perform actions
        actions_dict = {"+": self.add, "-": self.subtrackt, "*": self.multiply, "/": self.divide}
        numbers_stack = []
        for token in tokens:
            if token not in actions_dict:
                numbers_stack.append(int(token))
            else:
                item_2 = numbers_stack.pop()
                item_1 = numbers_stack.pop()
                res = actions_dict[token](item_1, item_2)
                numbers_stack.append(res)
        return numbers_stack.pop()

    def add(self, item_1, item_2):
        print(f"calling {item_1} + {item_2} = {item_1 + item_2}")
        return item_1 + item_2

    def subtrackt(self, item_1, item_2):
        print(f"calling {item_1} - {item_2} = {item_1 - item_2}")
        return item_1 - item_2

    def divide(self, item_1, item_2):
        res = item_1 // item_2
        if res < 0 and item_1 % item_2 != 0:
            res += 1
        print(f"calling {item_1} // {item_2} = {res}")
        return res

    def multiply(self, item_1, item_2):
        print(f"calling {item_1} * {item_2} = {item_1 * item_2}")
        return item_1 * item_2


def some_test():
    a = Solution()
    input_board = ["4", "-2", "/", "2", "-3", "-", "-"]
    print(
        a.evalRPN(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
