# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#dfs and keep track of depth level and parent? or could jsut do BFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = collections.deque()
        q.append((root, None))
        currDepth = 0
        xDepth, yDepth = 0, 0
        xParent, yParent = None, None

        if root.val == x or root.val == y:
            return False

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                currNode = curr[0]
                if currNode.val == x:
                    xDepth = currDepth
                    xParent = curr[1]
                if currNode.val == y:
                    yDepth = currDepth
                    yParent = curr[1]
                if currNode.left:
                    q.append((currNode.left, currNode))
                if currNode.right:
                    q.append((currNode.right, currNode))
            currDepth += 1
            if xParent != None and yParent != None:
                break

        return xParent.val != yParent.val and xDepth == yDepth


        