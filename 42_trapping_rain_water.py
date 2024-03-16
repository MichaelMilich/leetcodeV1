class Solution:
    def trap(self, height: [int]) -> [int]:
        local_maximums = []
        res = 0
        if len(height) < 3:
            return 0
        # first lets get the local maximums
        for index, value in enumerate(height):
            if index == 0:
                if value > height[index + 1]:
                    local_maximums.append((index, value))
            elif index == len(height) - 1:
                if value > height[index - 1]:
                    local_maximums.append((index, value))
            else:
                if value > height[index + 1] and value > height[index - 1]:
                    local_maximums.append((index, value))
                elif value>= height[index+1] and value > height[index - 1]:
                    local_maximums.append((index, value))
                elif value > height[index + 1] and value >= height[index - 1]:
                    local_maximums.append((index, value))
        # local_maximums.sort(key=lambda x: x[1], reverse=True)
        if len(local_maximums) <= 1:
            return res
        print(f"local_maximums = {local_maximums}")
        local_maximums2 = [local_maximums[0]]

        # lets find local maximum that is between two local maximums higher than him
        idx = 1

        while idx < len(local_maximums) - 1:
            if not self.is_between_larger_maximums(local_maximums,idx):
                print(f"local maximum number {idx} is not between larger maximums")
                print(f"local maximum number {idx} = {local_maximums[idx]}")
                local_maximums2.append(local_maximums[idx])
            idx+=1

        local_maximums2.append(local_maximums[-1])
        print(f"local_maximums2 = {local_maximums2}")

        # now lets go between each pair of local maximums and add between them

        start = 0
        stop = 1
        while stop < len(local_maximums2):
            start_idx = local_maximums2[start][0]
            stop_idx = local_maximums2[stop][0]
            start_val = local_maximums2[start][1]
            stop_val = local_maximums2[stop][1]
            top = min(start_val, stop_val)
            add = 0
            print(f"top = {top}")
            i = start_idx
            while i < stop_idx - 1:
                i += 1
                add += max(top - height[i], 0)

            print(f" between {start_idx} and {stop_idx} adding {add}")
            res += add
            start += 1
            stop += 1
        return res

    def is_between_larger_maximums(self, local_maximums, lookup_idx):
        """
        call this function only for  0<lookup_idx < len(local_maximums)-1
        :param local_maximums:
        :param lookup_idx:
        :return:
        """
        local_h = local_maximums[lookup_idx][1]
        before = lookup_idx - 1
        after = lookup_idx + 1
        before_flag = False
        after_flag = False
        while before >= 0:
            before_h = local_maximums[before][1]
            if before_h > local_h:
                print(f"before : {before_h} >{local_h}")
                before_flag = True
                break
            before -= 1
        while after <= len(local_maximums) - 1:
            after_h = local_maximums[after][1]
            if after_h > local_h:
                print(f"after : {after_h} >{local_h}")
                after_flag = True
                break
            after += 1
        return before_flag and after_flag


def some_test():
    a = Solution()
    input_board = [5,5,1,7,1,1,5,2,7,6]
    print(input_board)
    print(
        a.trap(input_board)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
