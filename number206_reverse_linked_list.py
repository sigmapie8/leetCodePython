# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parentNode = None
        currNode = head
        
        while(currNode is not None):
            nextNode = currNode.next
            currNode.next = parentNode
            parentNode = currNode
            currNode = nextNode
        
        return parentNode
