class Solution:
    def maxProduct(self, nums: [int]) -> int:
        """
        Given an integer array nums, find a subarray that has the largest product, and return the product.

        The test cases are generated so that the answer will fit in a 32-bit integer.
        :param nums:
        :return:
        """
        res = max(nums)
        theMin, theMax = 1, 1
        for num in nums:
            if num == 0:
                theMin, theMax = 1, 1
                continue
            temp = theMax * num
            theMax = max(temp, theMin * num, num)
            theMin = min(temp, theMin * num, num)
            res = max(res, theMax)
        return res


def some_test():
    a = Solution()
    input_case = [3, 1, -2, 2, 2, 1, -2, -3]
    target = 1
    print(input_case)
    res = a.maxProduct(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
