

class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        new_set = set()
        for number in nums:
            if number in new_set:
                return True
            new_set.add(number)
        return False


def some_test(nums: [int]):
    # Use a breakpoint in the code line below to debug your script.
    print(f"the list is {nums} , its length is {len(nums)}")
    print(f"the list set is {set(nums)} , its length is {len(set(nums))}")
    print(set(nums))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test([1,2,3,4,5,6,7,8,9,1])