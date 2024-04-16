class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        """
        Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen numbers sum to target.
        You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times.
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations that sum up to target is
         less than 150 combinations for the given input.

        :param candidates:
        :param target:
        :return:
        """
        res = []
        temp_arr = []

        def subset_idx(idx: int, new_arr: [int], new_target: int):
            if new_target < 0:
                return
            if new_target == 0:
                res.append(new_arr.copy())
                return
            if idx >= len(candidates):
                return
            new_arr.append(candidates[idx])
            subset_idx(idx, new_arr, new_target - candidates[idx])
            new_arr.remove(candidates[idx])
            while idx < len(candidates)-1:
                idx += 1
                new_arr.append(candidates[idx])
                subset_idx(idx, new_arr, new_target - candidates[idx])
                new_arr.remove(candidates[idx])

        subset_idx(0, temp_arr, target)
        return res


def some_test():
    a = Solution()
    input_board = [2,3,5]
    target = 8
    print(input_board)
    res = a.combinationSum(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
