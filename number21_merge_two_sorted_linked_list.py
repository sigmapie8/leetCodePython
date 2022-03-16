# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        currNode1 = list1
        currNode2 = list2
        resultNode = ListNode()
        resultNodeHead = resultNode
        while(currNode1 is not None and currNode2 is not None):
            if(currNode1.val < currNode2.val):
                resultNode.next = currNode1
                currNode1 = currNode1.next
            else:
                resultNode.next = currNode2
                currNode2 = currNode2.next
            resultNode = resultNode.next
        
        while(currNode1 is not None):
            resultNode.next = currNode1
            currNode1 = currNode1.next
            resultNode = resultNode.next
        
        while(currNode2 is not None):
            resultNode.next = currNode2
            currNode2 = currNode2.next
            resultNode = resultNode.next
            
        return resultNodeHead.next
