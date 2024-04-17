import heapq
import math


class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        """
        Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
        and an integer k, return the k closest points to the origin (0, 0).

        The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
        You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
        :param points:
        :param k:
        :return:
        """
        res_dict = {}
        dist = []
        res = []
        temp =set()
        for point in points:
            val = (-1)*math.sqrt(point[0] ** 2 + point[1] ** 2)
            if val not in res_dict:
                res_dict[val]=[point]
            else:
                res_dict[val].append(point)

        for key in res_dict:
            for i in range(len(res_dict[key])):
                dist.append(key)
        heapq.heapify(dist)
        while len(dist) > k:
            heapq.heappop(dist)

        for dist_point in dist:
            if dist_point not in temp:
                res.extend(res_dict[dist_point])
            temp.add(dist_point)
        return res


def some_test():
    a = Solution()
    input_board = [[1,3],[-2,2],[2,-2]]
    target = 2
    print(input_board)
    res = a.kClosest(input_board, target)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
