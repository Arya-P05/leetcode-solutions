from typing import Optional

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head
        
        odd = ListNode(0, None)
        even = ListNode(0, None)
        odd_ptr = odd
        even_ptr = even
        idx = 1

        while (head is not None):
            if (idx % 2 == 0):
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            
            head = head.next
            idx += 1
        
        even_ptr.next = None
        odd_ptr.next = even.next

        return odd.next