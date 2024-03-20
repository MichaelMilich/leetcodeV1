class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        You are given an m x n integer matrix matrix with the following two properties:
            *) Each row is sorted in non-decreasing order
            *) The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.
        You must write a solution in O(log(m * n)) time complexity.
        :param matrix:
        :param target:
        :return:
        """
        n = len(matrix)
        start = 0
        stop = n - 1
        while start <= stop:
            middle = (stop - start) // 2 + start
            if target < matrix[middle][0]:
                stop = middle - 1
            elif target > matrix[middle][-1]:
                start = middle + 1
            elif matrix[middle][0] <= target <= matrix[middle][-1]:
                return True if self.search(matrix[middle], target) != -1 else False

        return False

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


def some_test():
    a = Solution()
    input_board = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(input_board)
    res = a.searchMatrix(input_board,target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
