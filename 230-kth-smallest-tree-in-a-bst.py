# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # smallest = all the way on the left
        # pre order traversal?
        # O(n) - i don't think it can be logn because you don't know how many nodes there are

        countK = [0]
        def dfs(root):
            if root == None:
                return -1
            left = dfs(root.left)
            if left != -1:
                return left
            countK[0] += 1
            if countK[0] == k:
                return root.val
            right = dfs(root.right)
            if right != -1:
                return right
            return -1

        return dfs(root)

