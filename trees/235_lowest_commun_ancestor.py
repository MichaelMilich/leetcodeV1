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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
        According to the definition of LCA on Wikipedia:
        “The lowest common ancestor is defined between two nodes p and q as thelowest node in T that has both p and q
         as descendants (where we allow a node to be a descendant of itself).”

        Constraints:
            The number of nodes in the tree is in the range [2, 105].
            -109 <= Node.val <= 109
            All Node.val are unique.
            p != q
            p and q will exist in the BST.
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p.val <= root.val <= q.val:
            return root
        if p.val >= root.val >= q.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        return None


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
    input_board1 = [2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]
    corrected_input = create_complete_binary_tree(input_board1)

    print(f"input board = {input_board1}")
    print(f"correct form = {corrected_input}")
    input_tree = create_binary_tree(corrected_input)

    print(input_tree)
    res = a.isBalanced(input_tree)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
