from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = ListNode(0)
        ans_pointer = answer

        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            carry = total // 10

            ans_pointer.next = ListNode(total % 10)
            ans_pointer = ans_pointer.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return answer.next
            