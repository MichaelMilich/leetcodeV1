# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

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
    def maxPathSum(self, root: TreeNode) -> int:
        """
        A path in a binary tree is:
            a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
        A node can only appear in the sequence at most once.
        Note that the path does not need to pass through the root.
        The path sum of a path is the sum of the node's values in the path.
        Given the root of a binary tree, return the maximum path sum of any non-empty path.
        :param root:
        :return:
        """
        max_path = root.val

        def check_path(root: TreeNode):
            nonlocal max_path
            if not root or root.val is None:
                return None
            temp = check_path(root.left)
            left_path = root.val if temp is None else root.val + temp
            temp = check_path(root.right)
            right_path = root.val if temp is None else root.val + temp
            max_path = max(max_path, left_path, right_path, left_path + right_path - root.val, root.val)
            return max(left_path, right_path, root.val)

        check_path(root)
        return max_path


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
            dict_create[left].parent = dict_create[key]
        if right in dict_create:
            dict_create[key].right = dict_create[right]
            dict_create[right].parent = dict_create[key]

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
    input_board1 = [-10,9,20,None,None,15,7]
    corrected_input = create_complete_binary_tree(input_board1)

    print(f"input board = {input_board1}")
    print(f"correct form = {corrected_input}")
    input_tree = create_binary_tree(corrected_input)

    print(input_tree)
    res = a.maxPathSum(input_tree)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
