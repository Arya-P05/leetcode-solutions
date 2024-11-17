from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        num_goodNodes = 0

        q = collections.deque([(root, float(-inf))])

        while q:
            node, max_val = q.popleft()

            if node.val >= max_val:
                num_goodNodes += 1
            if node.left:
                q.append((node.left, max(max_val, node.val)))
            if node.right:
                q.append((node.right, max(max_val, node.val)))
        
        return num_goodNodes

