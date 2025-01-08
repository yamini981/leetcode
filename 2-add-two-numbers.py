# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        curr = l1
        mult = 1
        while curr:
            num1 += mult * curr.val
            mult *= 10
            curr = curr.next

        curr = l2
        mult = 1
        while curr:
            num2 += mult * curr.val
            curr = curr.next
            mult*= 10

        total = num1 + num2

        head = ListNode(total % 10)
        total = total // 10
        curr = head

        while total > 0:
            curr.next = ListNode(total % 10)
            total = total // 10
            curr = curr.next

        return head
