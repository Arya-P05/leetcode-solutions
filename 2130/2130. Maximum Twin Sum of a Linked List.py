from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head_ptr = head
        vals = []

        while (head_ptr is not None):
            vals.append(head_ptr.val)
            head_ptr = head_ptr.next

        n = len(vals)
        max_sum = 0

        for idx, value in enumerate(vals):
           if idx <= ((n / 2) - 1):
                twin_idx = n - 1 - idx

                temp_sum = vals[idx] + vals[twin_idx]

                max_sum = max(max_sum, temp_sum)
        
        return max_sum


