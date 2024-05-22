from collections import Counter


class Solution:
    def canPartition(self, nums: [int]) -> bool:
        """
        Given an integer array nums,
        return true if you can partition the array into two subsets such that -
            the sum of the elements in both subsets is equal or false otherwise.
        :param nums:
        :return:
        """
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        n = len(nums)
        og_target = total_sum // 2
        q = {0}
        temp_q = set()
        for i in range(n - 1, -1, -1):
            for element in q:
                temp_q.add(element)
                if nums[i] + element == og_target:
                    return True
                if nums[i] + element < og_target:
                    temp_q.add(nums[i] + element)
            q = temp_q
            temp_q = set()
        return False


def some_test():
    a = Solution()
    input_case = [1, 5, 11, 5]
    target = 1
    print(input_case)
    res = a.canPartition(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
