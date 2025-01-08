# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sameTree(self, p, q):
            if p and not q:
                return False
            if q and not p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            
            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)

            return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot == None:
            return True
        if root == None:
            return False
        if self.sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right