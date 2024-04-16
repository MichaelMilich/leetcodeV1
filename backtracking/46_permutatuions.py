class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        """
        Given an array nums of distinct integers,
        return all the possible permutations. You can return the answer in any order.

        Constraints:
            1 <= nums.length <= 6
            -10 <= nums[i] <= 10
            All the integers of nums are unique.
        :param nums:
        :return:
        """
        res = []
        temp_arr = []

        def subset_idx(new_nums: [int], new_arr: [int]):
            if not new_nums:
                res.append(new_arr.copy())
                return
            for idx in range(len(new_nums)):
                new_arr.append(new_nums[idx])
                subset_idx(new_nums[:idx] + new_nums[idx + 1:], new_arr)
                new_arr.remove(new_nums[idx])

        subset_idx(nums, temp_arr)
        return res


def some_test():
    a = Solution()
    input_board = [1, 2, 3]
    target = 8
    print(input_board)
    res = a.permute(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
