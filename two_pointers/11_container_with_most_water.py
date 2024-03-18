class Solution:
    def maxArea(self, height: [int]) -> int:
        """
        You are given an integer array height of length n.
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        Notice that you may not slant the container.
        :param height:
        :return:
        """
        start = 0
        stop = len(height) - 1
        max_area =0
        while start < stop:
            start_h = height[start]
            stop_h = height[stop]
            area = (stop - start) * min(start_h, stop_h)
            if max_area <area:
                max_area=area
            if start_h < stop_h:
                start += 1
            else:
                stop -= 1
        return max_area


def some_test():
    a = Solution()
    input_board = [1,8,6,2,5,4,8,3,7]
    print(
        a.maxArea(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
