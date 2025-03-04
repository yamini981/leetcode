# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pTravelled = []
        qTravelled = []

        def dfs(node, desiredVal, array):
            array.append(node)
            if node.val == desiredVal:
                return node
            if node.left:
                found = dfs(node.left, desiredVal, array)
                if found == None:
                    del array[-1]
                else:
                    return node
            if node.right:
                found = dfs(node.right, desiredVal, array)
                if found == None:
                    del [array[-1]]
                else:
                    return node

            return None
        dfs(root, p.val, pTravelled)
        dfs(root, q.val, qTravelled)

        if len(pTravelled) > len(qTravelled):
            for i in range(len(qTravelled) - 1, -1, -1):
                if pTravelled[i].val == qTravelled[i].val:
                    return pTravelled[i]
        else:
            for i in range(len(pTravelled) - 1, -1, -1):
                if pTravelled[i].val == qTravelled[i].val:
                    return pTravelled[i]
        return None

