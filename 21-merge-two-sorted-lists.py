# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        l = list1
        r = list2

        while l != None and r != None:
            if r.val <= l.val:
                curr.next = r
                r = r.next
            else: #l.val < r.val
                curr.next = l
                l = l.next
            
            curr = curr.next
        
        if l:
            curr.next = l
        if r:
            curr.next = r
        
        return dummy.next