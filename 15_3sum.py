class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        """
        Given an integer array nums,
        return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
        and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        :param nums:
        :return:
        """
        res = []
        value_dict = {}
        for num in nums:
            value_dict[num] = 1 + value_dict.get(num, 0)

        for index ,num in enumerate(nums):
            key1,key2 = self.twoSum(value_dict,-num)
            if key2 is None:
                continue
            res.append([key1,key2,num])
        return res

    def twoSum(self, nums_dict: [int], target: int):
        print(nums_dict)
        for num in nums_dict:
            if target - num in nums_dict:
                if target -num == -target and nums_dict[target -num] == 1:
                    continue
                if num == -target and nums_dict[num] == 1:
                    continue
                if num == target - num and nums_dict[num] < 2:
                    continue
                if nums_dict[num] > 0 and nums_dict[target - num] > 0:
                    nums_dict[num] -= 1
                    nums_dict[target - num] -= 1
                    nums_dict[-target] -=1
                    return num, target - num
        return None, None


def some_test():
    a = Solution()
    input_board = [1,2,-2,-1]
    print(
        a.threeSum(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
