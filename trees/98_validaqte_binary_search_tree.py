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
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        A valid BST is defined as follows:
            *) The left subtree of a node contains only nodes with keys less than the node's key.
            *) The right subtree of a node contains only nodes with keys greater than the node's key.
            *) Both the left and right subtrees must also be binary search trees.
        :param root:
        :return:
        """
        is_binary_search = True

        def is_binary_search_node(root: TreeNode):
            nonlocal is_binary_search
            non_check_left = not root.left or root.left.val is None
            non_check_right = not root.right or root.right.val is None
            if non_check_left and non_check_right:
                return root, root.val, root.val

            # check the left node
            if root.left:
                left, left_min, left_max = is_binary_search_node(root.left)
            else:
                left, left_min, left_max = (None, None, None)
            # check the right node
            if root.right:
                right, right_min, right_max = is_binary_search_node(root.right)
            else:
                right, right_min, right_max = (None, None, None)

            if right_min is not None and left_max is not None:
                is_binary_search = is_binary_search and right_min > root.val > left_max and right.val > root.val > left.val
                return root, left_min, right_max
            elif right_min is not None:
                is_binary_search = is_binary_search and right_min > root.val and right.val > root.val
                return root, root.val, right_max
            elif left_max is not None:
                is_binary_search = is_binary_search and root.val > left_max and root.val > left.val
                return root, left_min, root.val

        is_binary_search_node(root)
        return is_binary_search


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
    input_board1 = [5,1,4,None,None,3,6]
    corrected_input = create_complete_binary_tree(input_board1)

    print(f"input board = {input_board1}")
    print(f"correct form = {corrected_input}")
    input_tree = create_binary_tree(corrected_input)

    print(input_tree)
    res = a.isValidBST(input_tree)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
