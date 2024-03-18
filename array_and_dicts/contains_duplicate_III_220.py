class Solution:

    # todo : refactor this and make it faster, 95% of all who answered this gave a code that runs faster
    def containsNearbyAlmostDuplicate(self, nums: [int], indexDiff: int, valueDiff: int) -> bool:
        """
        You are given an integer array nums and two integers indexDiff and valueDiff.
        Find a pair of indices (i, j) such that:
            1) i!=j
            2) abs(i-j) <=indexDiff
            3) abs(nums[i] -nums[j]) <=valueDiff
        :param nums: list of integers
        :param indexDiff: the index difference in the array
        :param valueDiff: the value difference between two values
        :return: true if such pair exists or false otherwise.
        """
        # first lets throw out anything that is irrelevent
        if len(nums) <= 1:
            return False
        if indexDiff < 1:
            return False
        if valueDiff < 0:
            return False

        return self.save_code(nums,indexDiff,valueDiff)

    def containsNearbyDuplicateFaster(self, nums: [int], k: int) -> bool:
        """
        THIS IS THE FASTER VERSION

        Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
        such that nums[i] == nums[j] and abs(i - j) <= k
        :param nums: list of integers to check
        :param k: the span where we are looking for the doubles
        :return: true if there are ducplicates within any span k numbers of the list. false  otherwise.
        """
        # first lets call the edge case :
        if k == 0:
            return False
        set_dict = {}
        for index, number in enumerate(nums):
            if number in set_dict:
                if index - set_dict[number] <= k:
                    return True
            set_dict[number] = index
        return False

    def save_code(self, nums: [int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff == 0:
            return self.containsNearbyDuplicateFaster(nums, indexDiff)

        values_dict = {}

        for index, number in enumerate(nums):
            for value in values_dict.keys():
                if abs(number - value) <= valueDiff:
                    for val_index in values_dict[value]:
                        if abs(index - val_index) <= indexDiff:
                            return True
            if number not in values_dict:
                values_dict[number] = [index]
            else:
                if abs(index - values_dict[number][-1]) <= indexDiff:
                    return True
                values_dict[number].append(index)
        return False


def some_test():
    a = Solution()
    nums = [3,6,0,4]
    indexDiff = 2
    valueDiff = 2
    print(a.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))


def test_idea():
    nums = [1, 2, 4, 6, 7, 10, 20, 44]
    print(f"nums len = {len(nums)}")
    insert = 20
    a = IndexValueList(nums, len(nums) - 2)
    a.add_into_sorted_list(insert, 6)
    print(a.inner_list)
    print(f"nums len = {len(nums)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
