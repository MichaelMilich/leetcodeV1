class Solution:
    def search(self, nums: [int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order,and an integer target,
        write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.
        this runs abit slower but takes less space
        :param nums:
        :param target:
        :return:
        """
        left, right= 0, len(nums)-1

        while left<=right:
            middle = (left+right)//2
            if nums[middle]>target:
                right = middle -1
            elif nums[middle] <target:
                left=middle+1
            else:
                return middle
        return -1

    def search_req(self, nums: [int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order,and an integer target,
        write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.

        NOTE: this runs a little faster than the no requisition for some reason, however, it takes more memory
        :param nums:
        :param target:
        :return:
        """

        def req_search(target, start, stop):
            if stop == start:
                if target == nums[start]:
                    return start
                return -1
            if stop == start + 1:
                if target == nums[start]:
                    return start
                if target == nums[stop]:
                    return stop
                return -1

            middle = (stop + start) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                return req_search(target, middle, stop)
            else:
                return req_search(target, start, middle)

        return req_search(target, 0, len(nums) - 1)

def some_test():
    a = Solution()
    input_board = [-1,0,3,5,9,12]
    target = 2
    print(input_board)
    res = a.search(input_board,target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()