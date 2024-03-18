import itertools


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        :param n:
        :return:
        """
        stack =[]
        res = []

        def do_stuff(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return
            if open_count < n:
                stack.append("(")
                do_stuff(open_count+1,close_count)
                stack.pop()
            if close_count < open_count:
                stack.append(")")
                do_stuff(open_count , close_count+1)
                stack.pop()

        do_stuff(0,0)
        return res

    def first_try(self, n: int) -> [str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        didn't work - I ddin't account all possible cases
        :param n:
        :return:
        """
        i = 1
        n_dict = {1: ["()"]}
        n_set = set()
        while i <= n:
            i += 1
            if i not in n_dict:
                n_dict[i] = []
            for element in n_dict[i - 1]:
                if f"({element})" not in n_set:
                    n_dict[i].append(f"({element})")
                    n_set.add(f"({element})")
                if f"{element}()" not in n_set:
                    n_dict[i].append(f"{element}()")
                    n_set.add(f"{element}()")
                if f"(){element}" not in n_set:
                    n_dict[i].append(f"(){element}")
                    n_set.add(f"(){element}")
        return n_dict[n]


def some_test():
    a = Solution()
    input_board = 4
    res = a.generateParenthesis(input_board)
    print(input_board)
    print(res)
    print("(())(())" in res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
