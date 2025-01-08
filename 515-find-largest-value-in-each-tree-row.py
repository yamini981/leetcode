# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        q = collections.deque()

        q.append(root)
        maxInRow = 0
        while q:
            first = True
            for i in range(len(q)):
                curr = q.popleft()
                if first:
                    first = False
                    maxInRow = curr.val
                else:
                    maxInRow = max(maxInRow, curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ret.append(maxInRow)
        
        return ret
                
                
                
