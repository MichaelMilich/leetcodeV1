class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        """
        Given a collection of candidate numbers (candidates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.

        Note: The solution set must not contain duplicate combinations.

        :param candidates:
        :param target:
        :return:
        """
        res = []
        temp_arr = []
        candidates.sort()
        print(candidates)

        def subset_idx(idx: int, new_arr: [int], new_target: int):
            if new_target < 0:
                return
            if new_target == 0:
                res.append(new_arr.copy())
                return
            if idx >= len(candidates):
                return

            new_arr.append(candidates[idx])
            subset_idx(idx + 1, new_arr, new_target - candidates[idx])
            new_arr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            subset_idx(idx + 1, new_arr, new_target)

        subset_idx(0, temp_arr, target)
        return res


def some_test():
    a = Solution()
    input_board = [2,5,2,1,2]
    target = 5
    print(input_board)
    res = a.combinationSum2(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
