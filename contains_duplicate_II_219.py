class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        """
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
                set_dict[number].append(index)
            else:
                set_dict[number] = [index]

        lists = list(filter(lambda a_list: len(a_list) > 1, set_dict.values()))
        print(lists)
        if len(lists) == 0:
            return False

        for a_list in lists:
            i = 0
            j = 1
            while j < len(a_list):
                if a_list[j] - a_list[i] <= k:
                    return True
                i += 1
                j += 1

        return False

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
                if index - set_dict[number] <=k:
                    return True
            set_dict[number] = index
        return False

def some_test():
    a = Solution()
    print(a.containsNearbyDuplicate([1, 2, 3, 1, 2, 10, 2, 4, 5, 6, -7, 8, -7], 1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
