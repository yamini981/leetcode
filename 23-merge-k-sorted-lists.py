# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # can do merge 2 lists then just repeat for every list...
        # I believe this would be O(n * k)
        if len(lists) == 0:
            return None
            

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None

                mergedLists.append(self.merge2Lists(l1, l2))
            lists = mergedLists
        return lists[0]

    def merge2Lists(self, list1, list2):
            dummy = ListNode()
            tail = dummy
            p1 = list1
            p2 = list2
            while p1 and p2:
                if p1.val <= p2.val:
                    tail.next = p1
                    p1 = p1.next
                else:
                    tail.next = p2
                    p2 = p2.next
                tail = tail.next
            
            while p1 != None:
                tail.next = p1
                p1 = p1.next
                tail = tail.next
            while p2 != None:
                tail.next = p2
                p2 = p2.next
                tail = tail.next
            
            return dummy.next