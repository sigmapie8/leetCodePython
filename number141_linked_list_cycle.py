# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head
        
        if(head is None or head.next is None):
            return False
        
        if(head.next.next is not None and head is head.next.next):
            return True
        
        while(fastPointer.next is not None and fastPointer.next.next is not None):
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if(slowPointer is fastPointer):
                return True
            
        return False
        
