class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        """
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        There is only one repeated number in nums, return this repeated number.
        You must solve the problem without modifying the array nums and uses only constant extra space.
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 2:
            return nums[0]
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        mu =0
        slow2 =0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            mu+=1

        return slow2

def some_test():
    a = Solution()
    input_board = [2,5,9,6,9,3,8,9,7,1]
    target = 8
    print(input_board)
    res = a.findDuplicate(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
