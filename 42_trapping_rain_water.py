class Solution:
    def trap(self, height: [int]) -> [int]:
        left_index = 0
        left_max = height[left_index]
        right_index = len(height) - 1
        right_max = height[right_index]
        sum = 0

        while left_index < right_index:
            if right_max < left_max:
                sum += max(0, right_max - height[right_index])
                right_index -= 1
                if right_max < height[right_index]:
                    right_max = height[right_index]
            else:  # left_max <= right_max
                sum += max(0, left_max - height[left_index])
                left_index += 1
                if left_max < height[left_index]:
                    left_max = height[left_index]
        return sum


def some_test():
    a = Solution()
    input_board = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
    print(input_board)
    print(
        a.trap(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
