class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        """
        Given an array of integers heights representing the histogram's bar height where the width of each bar is 1
        return the area of the largest rectangle in the histogram.
        :param heights:
        :return:
        """
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                temp_i, temp_h = stack.pop()
                area = temp_h * (index - temp_i)
                if max_area < area:
                    max_area = area
                start = temp_i
            stack.append((start, height))

        while stack:
            temp_i, temp_h = stack.pop()
            area = temp_h * (len(heights) - temp_i)
            if max_area < area:
                max_area = area
        return max_area

    def obvious_solution(self, heights: [int]) -> int:
        """
        Given an array of integers heights representing the histogram's bar height where the width of each bar is 1
        return the area of the largest rectangle in the histogram.
        :param heights:
        :return:
        """
        # lets start with the most obvious solution, finding the max in O(n^2)
        max_height_list = []
        max_volume_list = []
        abs_max = 0
        index1 = 0
        while index1 < len(heights):
            max_height_list.append(heights[index1])
            max_volume_list.append(heights[index1])
            for index2 in range(index1 + 1, len(heights)):
                min_top = min(max_height_list[index1], heights[index2])
                max_height_list[index1] = min_top
                new_volume = min_top * (1 + index2 - index1)
                if new_volume > max_volume_list[index1]:
                    max_volume_list[index1] = new_volume
            if abs_max < max_volume_list[index1]:
                abs_max = max_volume_list[index1]
            index1 += 1
        print(f"max_volume_list = {max_volume_list}")
        return abs_max


def some_test():
    a = Solution()
    input_board = [2,3]
    print(input_board)
    res = a.largestRectangleArea(input_board)

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
