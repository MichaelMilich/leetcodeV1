class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        """
        Given an integer array nums,
        return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.
        :param nums:
        :return:
        """
        res = [1 for x in nums]
        pre =1
        post=1
        for i in range(len(nums)):
            res[i] =pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res


def some_test():
    a = Solution()
    print(
        a.productExceptSelf([1, 2, 3, 4])
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
