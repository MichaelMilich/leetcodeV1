class Solution:
    def rob(self, nums: [int]) -> int:
        """
        You are a professional robber planning to rob houses along a street.
        Each house has a certain amount of money stashed,
        the only constraint stopping you from robbing each of them is that adjacent houses have security systems
        connected and it will automatically contact the police
        if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house,
         return the maximum amount of money you can rob tonight without alerting the police.
        :param nums:
        :return:
        """
        n = len(nums)
        new_nums = [0 for _ in nums]
        for i in range(n - 1, -1, -1):
            if i == n - 1 or i == n - 2:
                new_nums[i] = nums[i]
            else:
                new_nums[i] = nums[i] +max(new_nums[i+2:])
        print(new_nums)
        return max(new_nums[0:2])


def some_test():
    a = Solution()
    input_case = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(input_case)
    res = a.rob(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
