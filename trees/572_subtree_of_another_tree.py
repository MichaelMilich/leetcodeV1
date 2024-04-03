# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = f"TreeNode [ val = {self.val} , "
        if self.left is None:
            s += "left = None , "
        else:
            s += f"\n left = ({self.left}) , "
        if self.right is None:
            s += "right = None , "
        else:
            s += f"\n right = ({self.right}) ]"
        return s

    def __repr__(self):
        s = f"TreeNode [ val = {self.val} , left = ({self.left}) , right = ({self.right}) ]"
        if self.left is None:
            s += "left = None , "
        else:
            s += f"left = (\n{self.left}) , "
        if self.right is None:
            s += "left = None , "
        else:
            s += f"left = (\n{self.right}) ]"
        return s


class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        res_left = self.isSubtree(root.left, subRoot)
        res_right = self.isSubtree(root.right, subRoot)
        return res_left or res_right

    def isSameTree(self, root_1: TreeNode, root_2: TreeNode) -> bool:
        if root_1 is None:
            return root_2 is None
        if root_2 is None:
            return root_1 is None
        if root_1.val != root_2.val:
            return False
        res_left = self.isSameTree(root_1.left, root_2.left)
        res_right = self.isSameTree(root_1.right, root_2.right)
        return res_left and res_right


def create_binary_tree(input_board: [int]):
    n = len(input_board)
    if n == 0:
        return None
    dict_create = {}

    for index in range(n):
        dict_create[index] = TreeNode(val=input_board[index])

    for key in dict_create:
        if dict_create[key].val is None:
            continue
        left = 2 * key + 1
        right = 2 * key + 2
        if left in dict_create:
            dict_create[key].left = dict_create[left]
        if right in dict_create:
            dict_create[key].right = dict_create[right]

    return dict_create[0]


def create_complete_binary_tree(input_board: [int]):
    new_board_dict = copy.copy(input_board)
    a = []
    index = 0
    n = len(input_board)
    while index < n:
        val = new_board_dict[index]
        if val is None:
            right = 2 * index + 2
            left = 2 * index + 1
            if right < n:
                new_board_dict.insert(right, None)
            if left < n:
                new_board_dict.insert(left, None)
        index += 1
    return new_board_dict


def some_test():
    a = Solution()
    input_board1 = [3,4,5,1,2,None,None,None,None,0]
    corrected_input1 = create_complete_binary_tree(input_board1)

    input_board2 = [4,1,2]
    corrected_input2 = create_complete_binary_tree(input_board2)

    input_tree1 = create_binary_tree(corrected_input1)
    input_tree2 = create_binary_tree(corrected_input2)

    res = a.isSubtree(input_tree1,input_tree2)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
