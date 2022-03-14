# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastNode = head
        slowNode = head
        
        while(fastNode.next is not None):
            if(fastNode.next.next is not None):
                fastNode = fastNode.next.next
                slowNode = slowNode.next
            elif(fastNode.next is not None):
                fastNode = fastNode.next
                slowNode = slowNode.next
            
        return slowNode
