from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []

        def ln(root, arr):
            if root and root.left is None and root.right is None:
                arr.append(root.val)
            elif root.left and root.right:
                ln(root.left, arr)
                ln(root.right, arr)
            elif root.left:
                ln(root.left, arr)
            elif root.right:
                ln(root.right, arr)

        if root1 is None and root2 is None:
            return False
        else:
            ln(root1, r1)
            ln(root2, r2)

            return r1 == r2
