class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing:
            a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction
        If you cannot achieve any profit, return 0.


        :param prices:
        :return:
        """
        # this algorithm works, takes memory O(1) but also time of O(n^2)
        # it makes it very slow but better in memory.... there is a better solution
        max_price = 0
        profit = 0
        n = len(prices) - 1
        index = n
        while index > 0:
            if prices[index] > max_price:
                max_price = prices[index]
                max_price_index = index
                profit = max(profit, max_price - min(prices[:max_price_index]))
            index -= 1
        return profit

    def maxProfit_shit_algo(self, prices: [int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing:
            a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction
        If you cannot achieve any profit, return 0.


        :param prices:
        :return:
        """
        # this algorithm is shit, it runs in O(n^3)
        n = len(prices) - 1
        max_profit = 0
        while n >= 1:
            start = 0
            while start + n <= len(prices) - 1:
                if prices[start] < prices[start + n]:
                    max_profit = max(max_profit, prices[start + n] - prices[start])
                start += 1
            n -= 1
        return max_profit

    def maxProfit_prev(self, prices: [int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing:
            a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction
        If you cannot achieve any profit, return 0.
        :param prices:
        :return:
        """
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        return max_profit


def some_test():
    a = Solution()
    input_board = [1, 2]
    target = 2
    print(input_board)
    res = a.maxProfit_prev(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
