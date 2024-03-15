class Solution:
    def trap(self, height: [int]) -> [int]:
        local_maximums = []
        res = 0
        # first lets get the local maximums
        for index, value in enumerate(height):
            if index == 0:
                if value >= height[index + 1]:
                    local_maximums.append((index, value))
            elif index == len(height) - 1:
                if value >= height[index - 1]:
                    local_maximums.append((index, value))
            else:
                if value >= height[index + 1] and value >= height[index - 1]:
                    local_maximums.append((index, value))

        print(f"local_maximums = {local_maximums}")
        # now lets go between each pair of local maximums and add between them
        if len(local_maximums) <= 1:
            return res
        start = 0
        stop = 1
        while stop < len(local_maximums):
            start_idx = local_maximums[start][0]
            stop_idx = local_maximums[stop][0]
            start_val = local_maximums[start][1]
            stop_val = local_maximums[stop][1]
            top = min(start_val, stop_val)
            add = 0
            print(f"top = {top}")
            i= start_idx
            while i < stop_idx-1:
                i += 1
                add += top - height[i]

            print(f" between {start_idx} and {stop_idx} adding {add}")
            res += add
            start += 1
            stop += 1
        return res


def some_test():
    a = Solution()
    input_board = [4,2,0,3,2,5]
    print(input_board)
    print(
        a.trap(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
