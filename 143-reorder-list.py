# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find second half of list
        if head.next == None:
            return head
        
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next

        # Reverse second half of list
        curr = second
        prev = None
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # Do swapping (draw it out if needed)
        currEnd = prev
        currStart = head
        while currEnd != None and currStart.next != currEnd:
            tmp1, tmp2 = currStart.next, currEnd.next
            currStart.next = currEnd
            currEnd.next = tmp1
            currStart, currEnd = tmp1, tmp2

        if currEnd == None:
            currStart.next = None