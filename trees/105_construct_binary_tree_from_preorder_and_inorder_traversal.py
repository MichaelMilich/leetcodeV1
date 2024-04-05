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
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        """
        Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
        and inorder is the inorder traversal of the same tree, construct and return the binary tree.

        Constraints:
            1 <= preorder.length <= 3000
            inorder.length == preorder.length
            -3000 <= preorder[i], inorder[i] <= 3000
            preorder and inorder consist of unique values.
            Each value of inorder also appears in preorder.
            preorder is guaranteed to be the preorder traversal of the tree.
            inorder is guaranteed to be the inorder traversal of the tree.

        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


def some_test():
    a = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    print(f"preorder = {preorder}")
    print(f"inorder = {inorder}")

    res = a.buildTree(preorder, inorder)
    print("************************")
    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()
