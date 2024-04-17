import heapq
import math


class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        """
        You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
        Each cycle or interval allows the completion of one task.
        Tasks can be completed in any order, but there's a constraint:
            identical tasks must be separated by at least n intervals due to cooling time.
        Return the minimum number of intervals required to complete all tasks.
        :param tasks:
        :param n:
        :return:
        """
        # todo : do this
        return 0



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
