# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time O(n) space is simple: use a hashset to track visited nodes. 
        
        # How to do O(1) space...
        # prev, curr -4 2
        # O(1) space could be just iterate until you've searched 10^4 nodes...
        # if you have done greater than that then confirmed cycle

        #  currIndex = 0
        # after visiting a node, set next to the head. If you ever end up at the head, you know there's a cycle

        s = head
        f = head

        while f != None and f.next != None:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


