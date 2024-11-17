from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# if the action on curr node is above left and right then its pre-order
# if the action on curr node is in between left and right then its in-order
# if the action on curr node is after left and right then its post-order

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def check_path(curr_sum, targetSum, root):
            if root is None:
                return 0

            curr_sum += root.val

            if curr_sum == targetSum:
                return 1 + check_path(curr_sum, targetSum, root.left) + check_path(curr_sum, targetSum, root.right)
            else:
                return check_path(curr_sum, targetSum, root.left) + check_path(curr_sum, targetSum, root.right)
        
        def dfs(root) -> int:
            if root is None:
                return 0
            else:
                count = check_path(0, targetSum, root)
                count += dfs(root.left)
                count += dfs(root.right)
            
            return count
                
        return dfs(root)
        