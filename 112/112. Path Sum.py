from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sumFound(root, curr, target):
            if root is None:
                return False
            elif ((curr + root.val) == target) and (root.left is None) and (root.right is None):
                return True 
            else:
                return sumFound(root.left, curr + root.val, target) or sumFound(root.right, curr + root.val, target)

        if (root is None):
            return False
        elif (root.val == targetSum) and (root.left is None) and (root.right is None):
            return True
        else:
            curr_sum = root.val
            return sumFound(root.left, curr_sum, targetSum) or sumFound(root.right, curr_sum, targetSum)
        