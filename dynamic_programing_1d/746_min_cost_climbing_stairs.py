class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        """
        you are given an integer array cost where cost[i] is the cost of ith step on a staircase.
        Once you pay the cost, you can either climb one or two steps.

        You can either start from the step with index 0, or the step with index 1.

        Return the minimum cost to reach the top of the floor.
        :param cost:
        :return:
        """
        start = 0
        n = len(cost)
        arr = [0] * (n + 1)
        idx = 2
        arr[0] = cost[0]
        arr[1] = cost[1]
        while idx < n:
            arr[idx] = cost[idx] + min(arr[idx-1],arr[idx-2])
            idx += 1
        arr[idx] = min(arr[idx-1],arr[idx-2])
        return arr[n]


def some_test():
    a = Solution()
    input_case = [1,100,1,1,1,100,1,1,100,1]
    print(input_case)
    res = a.minCostClimbingStairs(input_case)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
