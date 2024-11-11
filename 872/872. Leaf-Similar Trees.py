from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return []
            elif root.left is None and root.right is None:
                return [root.val]
            else:
                return dfs(root.left) + dfs(root.right)

        if root1 is None and root2 is None:
            return False
        else:
            return dfs(root1) == dfs(root2)
