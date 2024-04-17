import heapq
import math


class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element in the array.
        Note that it is the kth largest element in the sorted order, not the kth distinct element.


        :param nums:
        :param k:
        :return:
        """
        nums_set = [-x for x in nums]
        # for num in nums:
        #     if num not in nums_set:
        #         nums_set.add(num)
        num_list = nums_set
        idx = 0
        heapq.heapify(num_list)
        print(num_list)
        while idx <k-1:
            temp = heapq.heappop(num_list)
            # print(f"poped {temp}")
            idx += 1
        return heapq.heappop(num_list) * (-1)


def some_test():
    a = Solution()
    input_board = [3,2,1,5,6,4]
    target = 2
    print(input_board)
    res = a.findKthLargest(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
