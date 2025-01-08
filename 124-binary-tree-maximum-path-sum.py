# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = [root.val]
        def dfs(node):
            if node == None:
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            #splitMax (potential final return value)
            ret[0] = max(ret[0], node.val + leftMax + rightMax)

            #returnMax ( non split )
            return max(node.val + leftMax, node.val + rightMax)
        
        dfs(root)
        return ret[0]


