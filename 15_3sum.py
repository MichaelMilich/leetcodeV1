class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        """
        Given an integer array nums,
        return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
        and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        todo - redo this question again, write it down and understand how it works!
        :param nums:
        :return:
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

    def twoSum(self, numbers: [int], target: int) -> [int]:
        """
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
        find two numbers such that they add up to a specific target number

        Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
        Return the indices of the two numbers, index1 and index2,
        added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.
        Your solution must use only constant extra space.
        :param numbers:
        :param target:
        :return:
        """
        start = 0
        stop = len(numbers) - 1
        start_val = numbers[start]
        stop_val = numbers[stop]
        while start_val + stop_val != target and start < stop:
            if start_val + stop_val > target:
                stop -= 1
            else:
                start += 1
            start_val = numbers[start]
            stop_val = numbers[stop]

        if start_val + stop_val == target:
            print(f" {start_val} + {stop_val} = {target}")
            return start, stop
        else:
            return None, None


def some_test():
    a = Solution()
    input_board = [3, 0, -2, -1, 1, 2]
    print(
        a.threeSum(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
