# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length of node
        currNode = head
        length = 1
        while(currNode is not None and currNode.next is not None):
            currNode = currNode.next
            length += 1
        
        if(length == 1):
            return None
        
        parentNode = None
        currNode = head
        for i in range(length-n):
            parentNode = currNode
            currNode = currNode.next
        
        if(parentNode is not None and currNode is not None):
            parentNode.next = currNode.next
        elif(parentNode is None):
            head = currNode.next
        
        return head
