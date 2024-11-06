from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def areBothSymmetric(left, right):
            if (left is None and right is None):
                return True
            elif right is None or (left is None and right):
                return False
            elif (left.val != right.val):
                return False
            else:
                return areBothSymmetric(left.left, right.right) and areBothSymmetric(left.right, right.left)
        
        if (root is None):
            return True
        else:
            return areBothSymmetric(root.left, root.right)
