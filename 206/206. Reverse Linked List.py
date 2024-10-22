from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before_curr = None
        curr = head
        
        while (curr is not None):
            after_curr = curr.next
            curr.next = before_curr
            before_curr = curr
            curr = after_curr
        
        return before_curr