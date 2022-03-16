# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        parentNode = head
        currNode = None
        
        if(parentNode is None):
            return None
        elif(parentNode.next is None and parentNode.val == val):
            return None
        elif(parentNode.next is None):
            return head
        elif(parentNode.val == val):
            while(parentNode is not None and parentNode.val == val):
                parentNode = parentNode.next
                head = parentNode
            
            if(parentNode is not None): currNode = parentNode.next
        else:
            currNode = parentNode.next
        
        while(currNode is not None):
            if(currNode.val == val):
                parentNode.next = currNode.next    
                currNode = currNode.next
            else:
                parentNode = currNode
                currNode = currNode.next
        
        if(parentNode is None): return None
        return head
        
