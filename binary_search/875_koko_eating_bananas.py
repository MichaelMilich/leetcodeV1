class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        """
        Koko loves to eat bananas.
        There are n piles of bananas, the ith pile has piles[i] bananas.
        The guards have gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k.
        Each hour, she chooses some pile of bananas and eats k bananas from that pile.If the pile has less than k
        bananas, she eats all of them instead and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
        Return the minimum integer k such that she can eat all the bananas within h hours.
        :param piles:
        :param h:
        :return:
        """
        # todo: fix this
        if h == len(piles):
            return max(piles)

        right = max(piles)
        left = min_speed = 1
        slowest_time = self.hours_for_speed(piles, min_speed)
        if h == slowest_time:
            return min_speed

        res = right
        while left <= right:
            middle = (right - left) // 2 + left
            time = self.hours_for_speed(piles, middle)
            if time <= h:
                res = middle
                right = middle - 1
            elif time > h:
                left = middle + 1

        return res

    def hours_for_speed(self, piles, speed):
        sum = 0
        for pile in piles:
            sum += pile // speed + (pile % speed > 0)
        return sum


def some_test():
    a = Solution()
    input_board = [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589,
                   290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184]
    target = 823855818
    print(input_board)
    res = a.minEatingSpeed(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
