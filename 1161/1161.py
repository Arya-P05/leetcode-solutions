# Very jank solution with the changed tracker, will try to make something more robust

import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        app_queue = collections.deque([root])
        output_level = 1
        curr_level = 1
        
        max_total = root.val

        while app_queue:
            total = 0
            num_nodes = len(app_queue)

            for node_idx in range(num_nodes):
                curr_node = app_queue.popleft()

                if curr_node is not None:
                    total += curr_node.val

                    if curr_node.left:
                        app_queue.append(curr_node.left)
                    
                    if curr_node.right:
                        app_queue.append(curr_node.right)
            
            if total > max_total:
                max_total = total
                output_level = curr_level

            curr_level += 1

        return output_level
