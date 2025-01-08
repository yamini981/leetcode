# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #CAN'T BE EVEN EQUAL TO MAX, CAN'T BE EVEN EQUAL TO MIN
      
            
        def validate(root, minVal, maxVal):
            
            if root == None:
                return True

            left = validate(root.left, minVal, root.val)
            right = validate(root.right, root.val, maxVal)
            if root.val >= maxVal:
                return False
            if root.val <= minVal:
                return False
            
            
            return left and right

        return validate(root, -math.inf, math.inf)

        
