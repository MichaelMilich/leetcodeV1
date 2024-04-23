class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums)==1:
            return nums[0]
        rob1, rob2 = 0, 0

        for n in nums[1:]:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        rob21, rob22 = 0, 0

        for n in nums[:-1]:
            temp = max(n + rob21, rob22)
            rob21 = rob22
            rob22 = temp
        return max(rob2,rob22)


def some_test():
    a = Solution()
    input_case = [1,2,3,1]
    print(input_case)
    res = a.rob(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()