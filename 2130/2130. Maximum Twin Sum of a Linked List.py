from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head_ptr = head
        fast, slow = head, head

        while (fast is not None):
            slow = slow.next
            fast = fast.next.next

        prev, end = None, None

        while (slow is not None):
            end = slow.next
            slow.next = prev
            prev = slow
            slow = end
        
        max_sum = 0

        while (prev is not None):
            max_sum = max(max_sum, (head.val + prev.val))
            head = head.next
            prev = prev.next
        
        return max_sum
