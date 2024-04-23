class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        :param n:
        :return:
        """
        arr = [0 for i in range(n + 3)]
        idx = 0
        arr[idx] = 0
        arr[1]=1
        arr[2]=1
        while idx < n + 1:
            arr[idx + 1] += arr[idx]
            arr[idx + 2] += arr[idx]
            idx += 1
        print(arr)
        return arr[n]


def some_test():
    a = Solution()
    target = 10
    print(target)
    res = a.climbStairs(target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
