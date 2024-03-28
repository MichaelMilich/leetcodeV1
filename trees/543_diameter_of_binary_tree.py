# Definition for a binary tree node.
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, 2 + left + right)
            return 1 + max(left, right)
        dfs(root)
        return res

def create_binary_tree(input_board: [int]):
    n = len(input_board)
    if n == 0:
        return None
    dict_create = {}

    for index in range(n):
        dict_create[index] = TreeNode(val=input_board[index])

    for key in dict_create:
        left = 2 * key + 1
        right = 2 * key + 2
        if left in dict_create:
            dict_create[key].left = dict_create[left]
        if right in dict_create:
            dict_create[key].right = dict_create[right]

    return dict_create[0]


def some_test():
    a = Solution()
    input_board1 = [1, 2, 3, 4, 5]
    input_tree = create_binary_tree(input_board1)

    print(input_tree)
    res = a.diameterOfBinaryTree(input_tree)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
