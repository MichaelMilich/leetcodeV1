class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        """
        You are given an integer array coins representing coins of different denominations
        and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount.
        If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.
        :param coins:
        :param amount:
        :return:
        """
        if amount == 0:
            return 0
        coin_set = set()
        q = [0]
        next_level = []
        level_counter = 0
        while q or next_level:
            while q:
                element = q.pop()
                for coin in coins:
                    if element + coin == amount:
                        return level_counter+1
                    if element + coin not in coin_set and element+coin <=amount:
                        coin_set.add(element + coin)
                        next_level.append(element + coin)
            level_counter += 1
            q = next_level[:]
            next_level = []

        return -1


def some_test():
    a = Solution()
    input_case = [1]
    target = 1
    print(input_case)
    res = a.coinChange(input_case, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
