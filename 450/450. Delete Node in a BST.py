from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is not None:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                if root.right is None:
                    return root.left
                elif root.left is None:
                    return root.right
                else:
                    curr = root.right

                    while curr.left:
                        curr = curr.left
                    
                    root.val = curr.val
                    root.right = self.deleteNode(root.right, root.val)

        return root
    