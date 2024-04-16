class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        """
        Given an integer array nums of unique elements, return all possible subsets (the power set).
        The solution set must not contain duplicate subsets. Return the solution in any order.
        :param nums:
        :return:
        """
        res = []
        temp_arr = []

        def subset_idx(idx: int, new_arr: [int]):
            if idx >= len(nums):
                res.append(new_arr.copy())
                return
            new_arr.append(nums[idx])
            subset_idx(idx + 1, new_arr)
            new_arr.remove(nums[idx])
            subset_idx(idx + 1, new_arr)

        subset_idx(0, temp_arr)
        return res


def some_test():
    a = Solution()
    input_board = [1, 2, 3]
    target = 8
    print(input_board)
    res = a.subsets(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
