# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # just run DFS?
        if not root:
            return False
        def dfs(root, currSum):

            if root == None:
                return currSum == targetSum
            
            if root.left and not root.right:
                right = False
                left = dfs(root.left, currSum + root.val)
            elif root.right and not root.left:
                left = False
                right = dfs(root.right, currSum + root.val)
            else:
                left = dfs(root.left, currSum + root.val)
                right = dfs(root.right, currSum + root.val)

            return left or right

        return dfs(root, 0)