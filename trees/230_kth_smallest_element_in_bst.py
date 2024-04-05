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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Given the root of a binary search tree, and an integer k,
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
        :param root:
        :param k:
        :return:
        """
        nodes = []
        while root.left and root.left.val is not None:
            nodes.append(root)
            root = root.left
        while k > 1:
            if root.right:
                root = root.right
                while root.left and root.left.val is not None:
                    nodes.append(root)
                    root = root.left
                k -= 1
                continue
            if nodes:
                root = nodes.pop()
                k -= 1
                continue
        return root.val


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
    input_board1 = [50, 30, 60, 20, 40, None, None, 10, None, None, None, None, 19, 1]
    corrected_input = create_complete_binary_tree(input_board1)

    print(f"input board = {input_board1}")
    print(f"correct form = {corrected_input}")
    input_tree = create_binary_tree(corrected_input)

    print(input_tree)
    res = a.kthSmallest(input_tree, 3)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
