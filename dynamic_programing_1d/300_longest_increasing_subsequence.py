class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.
        :param nums:
        :return:
        """
        n = len(nums)
        arr = [1 for _ in nums]
        for i in range(n - 1, -1, -1):
            temp = [1]
            for j in range(i + 1, n):
                val_temp = nums[i]
                val_temp_2 = nums[j]
                if nums[j] > nums[i]:
                    temp.append(arr[j]+1)
            arr[i] = max(temp)
        return max(arr)


def some_test():
    a = Solution()
    input_case = [10, 9, 2, 5, 3, 7, 101, 18]
    print(input_case)
    res = a.lengthOfLIS(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
