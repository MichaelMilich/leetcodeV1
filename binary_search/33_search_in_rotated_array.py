class Solution:
    def search(self, nums: [int], target: int) -> int:
        """
        There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
        the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target
        return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        if n == 1:
            return 0 if target == nums[0] else -1
        if n == 2:
            return 0 if target == nums[0] else 1 if target == nums[1] else -1
        min_index = self.findMinIndex(nums)
        res_1 = self.b_search(nums[:min_index], target)
        res_2 = self.b_search(nums[min_index:], target)
        if res_1 != -1:
            return res_1
        if res_2 != -1:
            return res_2 +min_index
        return -1

    def b_search(self, nums: [int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order,and an integer target,
        write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.
        this runs abit slower but takes less space
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

    def findMinIndex(self, nums: [int]) -> int:
        """
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        For example, the array nums = [0,1,2,4,5,6,7] might become:
            *) [4,5,6,7,0,1,2] if it was rotated 4 times.
            *) [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], ..., a[n-2]].
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time.
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            # edge case 1) len of 1 - there is only one min
            return 0
        if n == 2:
            # edge case 2) only two element, we just compare
            return 0 if nums[0] < nums[1] else 1

        left, right = 0, n - 1
        if nums[left] < nums[right]:
            # edge case 3) if left < right there was no rotation, or there were n rotation.
            # at any rate it means that the array is back to original and min is left
            return left

        middle = (right - left) // 2 + left
        while left <= right:
            middle = (right - left) // 2 + left
            middle = middle + 1 if left == middle else middle
            if self.check_min(nums, middle, n):
                return middle
            if nums[middle] > nums[right]:
                left = middle
            elif nums[middle] < nums[left]:
                right = middle
        return middle

    def check_min(self, nums: [int], index: int, n: int):
        if 0 < index < n - 1:
            return nums[index - 1] > nums[index] and nums[index] < nums[index + 1]
        elif index == 0:
            return nums[-1] > nums[0] and nums[0] < nums[1]
        else:
            return nums[-2] > nums[-1] and nums[-1] < nums[0]


def some_test():
    a = Solution()
    input_board = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    print(input_board)
    res = a.search(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
