# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # bfs for each level, keep track of the level for the max sum
        maxLevel = 1
        maxLevelSum = root.val

        q = collections.deque()
        q.append(root)
        currLevel = 0

        while q:
            currLevel += 1
            currSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                currSum += node.val
            # print(currSum, currLevel)
            if currSum > maxLevelSum:
                maxLevelSum = currSum
                maxLevel = currLevel

        return maxLevel
