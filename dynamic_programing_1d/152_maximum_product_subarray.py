class Solution:
    def maxProduct(self, nums: [int]) -> int:
        """
        Given an integer array nums, find a subarray that has the largest product, and return the product.

        The test cases are generated so that the answer will fit in a 32-bit integer.
        :param nums:
        :return:
        """
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res


def some_test():
    a = Solution()
    input_case = [2,3,-2,4,4]
    target = 1
    print(input_case)
    res = a.maxProduct(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
