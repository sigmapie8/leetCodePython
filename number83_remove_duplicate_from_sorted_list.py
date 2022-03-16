# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parentNode = None
        currNode = None
        
        if(head is None):
            return None
        else:
            parentNode = head
            currNode = parentNode.next
        
        while(currNode is not None):
            if(parentNode.val == currNode.val):
                parentNode.next = currNode.next
                currNode = currNode.next
            else:
                parentNode = currNode
                currNode = currNode.next
        
        return head
