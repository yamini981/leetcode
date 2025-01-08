# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = collections.deque()

        count = 0
        q.append(root)
        while q:
            for i in range(len(q)):
                element = q.popleft()
                if element.right:
                    q.append(element.right)
                if element.left:
                    q.append(element.left)
            count += 1

        return count




