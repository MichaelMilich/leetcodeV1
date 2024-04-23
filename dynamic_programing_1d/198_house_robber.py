class Solution:
    def rob(self, nums: [int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


def some_test():
    a = Solution()
    input_case = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(input_case)
    res = a.rob(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
