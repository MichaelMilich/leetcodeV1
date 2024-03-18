class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        value_dict = {}
        freq_list = [[] for x in range(len(nums) + 1)]
        # the outer for is O(n) where n is length on nums
        for num in nums:
            if num not in value_dict:
                value_dict[num] = 1
            else:
                value_dict[num] += 1

        # this loop run O(n) in worst case
        result = []
        for key, value in value_dict.items():
            freq_list[value].append(key)

        # this loops run k times
        for i in range(len(freq_list) - 1, 0, -1):
            for j in range(len(freq_list[i])):
                result.append(freq_list[i][j])
                if len(result) == k:
                    return result


def some_test():
    a = Solution()
    print(a.topKFrequent([3, 0, 1, 0], 1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
