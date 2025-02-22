# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # calculate left length and right length of each node, and return
        # the add those up
        bestLength = 0
        def dfsLength(node):
            if node == None:
                return 0
            nonlocal bestLength
            leftLength = dfsLength(node.left)
            rightLength = dfsLength(node.right)
            bestLength = max(rightLength + leftLength, bestLength)
            return max(rightLength, leftLength) + 1
        dfsLength(root)
        return bestLength
            
        