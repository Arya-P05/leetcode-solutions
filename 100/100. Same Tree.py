from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None):
            return True
        elif (p and q is None) or (q and p is None):
            return False
        elif p.val != q.val or not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
            return False
        else:
            return True
        