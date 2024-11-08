from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_values = []
        app_q = collections.deque([root])

        while (app_q is not None):
            right_side_node = None
            num_nodes = len(app_q)

            for each_node in range(num_nodes):
                node = app_q.popleft()

                if (node is not None):
                    right_side_node = node
                    app_q.append(node.left)
                    app_q.append(node.right)
                
            if (right_side_node is None):
                right_side_values.append(right_side_node.val)
            
        return right_side_values
