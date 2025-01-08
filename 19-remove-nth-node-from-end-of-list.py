# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # problem is we dont' know where the end of the list is!
        # O(n) O(n) solution is trivial we just use a set
        # O(2n) O(1) solution can be found by counting total number of nodes

        
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        for _ in range(n):
            right = right.next
        
        while right != None:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

        
                