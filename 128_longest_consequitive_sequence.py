class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.
        :param nums:
        :return:
        """
        # edge case :
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        value_dict = {}
        sequance = {}

        for num in nums:
            value_dict[num] = 1 + value_dict.get(num, 0)

        for key in value_dict:
            if key - 1 not in value_dict:
                sequance[key] = 1

        for s in sequance:
            t = s + 1
            while t in value_dict:
                sequance[s] += 1
                t += 1

        max_count = 0
        for s in sequance:
            if max_count < sequance[s]:
                max_count = sequance[s]

        return max_count


def some_test():
    a = Solution()
    input_board = [-4,-4,2,-6,9,6,8,-6,-9,-1,9,5,2,-6,0]
    print(sorted(input_board))
    print(
        a.longestConsecutive(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
