# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        carry = 0
        while p1 or p2:
            digSum = 0
            if p1 and p2:
                digSum = p1.val + p2.val + carry
            elif p1:
                digSum = p1.val + carry

            if digSum > 9:
                carry = 1
            else:
                carry = 0
            if p1:
                p1.val = digSum % 10

            
            if not p1.next and (carry == 1 or (p2 and p2.next)):
                p1.next = ListNode()
            p1 = p1.next
            
            if p2:
                p2 = p2.next
                
        return l1
            