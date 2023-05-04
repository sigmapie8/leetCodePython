# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        firstNum = l1
        secondNum = l2
        carry = 0
        resultNode = ListNode()
        resultNodeStart = resultNode

        while(firstNum is not None or secondNum is not None):
            if(firstNum is None):
                firstNum = ListNode()
            
            if(secondNum is None):
                secondNum = ListNode()
            
            add = firstNum.val + secondNum.val + carry
            carry = add//10
            add = add%10

            resultNode.next = ListNode(val=add)
            resultNode = resultNode.next

            firstNum = firstNum.next
            secondNum = secondNum.next

        if(carry != 0):
            resultNode.next = ListNode(val=carry)

        resultNodeStart = resultNodeStart.next

        return resultNodeStart
