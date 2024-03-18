class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.
        :param nums: list of integers
        :param target: target number
        :return: list of indeces
        """
        if len(nums) == 2:
            return [0, 1]

        list_dict = {}
        for i in range(len(nums)):
            number = nums[i]
            if number in list_dict:
                list_dict[number].append(i)
            else:
                list_dict[number] = [i]
        return_list =[]
        for values in list_dict:
            if target- values in list_dict:
                if target-values !=values:
                    return_list.append(list_dict[values].pop(-1))
                    return_list.append(list_dict[target-values].pop(-1))
                    break
                elif len(list_dict[values]) >1:
                    return_list.append(list_dict[values].pop(-1))
                    return_list.append(list_dict[values].pop(-1))
                    break
                else:
                    continue

        return return_list


def some_test():
    a = Solution()
    print(a.twoSum([3,2,3], 6))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
