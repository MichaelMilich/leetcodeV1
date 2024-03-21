class Solution:
    def findMin(self, nums: [int]) -> int:
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
            return nums[0]
        if n == 2:
            # edge case 2) only two element, we just compare
            return min(nums[0], nums[1])

        left, right = 0, n - 1
        if nums[left] < nums[right]:
            # edge case 3) if left < right there was no rotation, or there were n rotation.
            # at any rate it means that the array is back to original and min is left
            return nums[left]

        middle = (right - left) // 2 + left
        while left <= right:
            middle = (right - left) // 2 + left
            middle = middle + 1 if left == middle else middle
            if self.check_min(nums, middle, n):
                return nums[middle]
            if nums[middle] > nums[right]:
                left = middle
            elif nums[middle] < nums[left]:
                right = middle
        return nums[middle]

    def check_min(self, nums: [int], index: int, n: int):
        if 0 < index < n - 1:
            return nums[index - 1] > nums[index] and nums[index] < nums[index + 1]
        elif index == 0:
            return nums[-1] > nums[0] and nums[0] < nums[1]
        else:
            return nums[-2] > nums[-1] and nums[-1] < nums[0]


def some_test():
    a = Solution()
    input_board = [2, 3, 1]
    target = 823855818
    print(input_board)
    res = a.findMin(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
