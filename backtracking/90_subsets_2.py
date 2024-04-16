class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        """
        Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
        The solution set must not contain duplicate subsets. Return the solution in any order.
        :param nums:
        :return:
        """
        nums.sort()
        res = []
        temp_arr = []

        def subset_idx(idx: int, new_arr: [int]):
            if idx >= len(nums):
                res.append(new_arr.copy())
                return

            new_arr.append(nums[idx])
            subset_idx(idx + 1, new_arr)
            new_arr.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            subset_idx(idx + 1, new_arr)

        subset_idx(0, temp_arr)
        return res


def some_test():
    a = Solution()
    input_board = [4, 1, 0]
    target = 8
    print(input_board)
    res = a.subsetsWithDup(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
