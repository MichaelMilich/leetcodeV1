import heapq


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        new_stones = [-x for x in stones]
        heapq.heapify(new_stones)
        while len(new_stones) >= 2:
            last1 = heapq.heappop(new_stones)
            last2 = heapq.heappop(new_stones)
            if last1 - last2 != 0:
                heapq.heappush(new_stones, last1 - last2)
        if len(new_stones)==0:
            return 0
        else:
            return heapq.heappop(new_stones) * (-1)


def some_test():
    a = Solution()
    input_board = [7, 6, 7, 6, 9]
    target = "ABCDEFGHI"
    print(input_board)
    res = a.lastStoneWeight(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
