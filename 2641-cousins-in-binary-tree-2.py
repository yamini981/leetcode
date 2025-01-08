# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS with tracking parents still a good idea - I think first traverse the tree once and sum all cousins, then traverse again
# to actually set the values
# actually not sure about that - some cousins will be missed on the first traversal through a level...
# maybe traverse each level twice? So you do BFS, traverse each level one way to get the total sum of the level
# then go back through but subtract sibling and self? (keep track of siblings instead of parents? Since there can only be one sibling)
# I think i cooked

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque()
        q.append((root, None))

        while q:
            levelSum = 0
            #sum calculating loop
            for _ in range(len(q)):
                # weird syntax but just makes sure the queue is maintained after the loop - still O(n)
                curr = q.popleft()
                levelSum += curr[0].val
                if curr[1]:
                    levelSum += curr[1].val
                q.append(curr)
            
            
            #set new values loop and add new items to queue
            for _ in range(len(q)):
                curr = q.popleft()
                
                # set values
                if curr[1]:
                    temp = curr[0].val
                    curr[0].val = levelSum - curr[0].val - curr[1].val
                    curr[1].val = levelSum - temp - curr[1].val
                else:
                    curr[0].val = levelSum - curr[0].val
                # add new kids to queue
                if curr[0].right and curr[0].left:
                    q.append((curr[0].left, curr[0].right))
                elif curr[0].right:
                    q.append((curr[0].right, None))
                elif curr[0].left:
                    q.append((curr[0].left, None))

                if curr[1]:
                    if curr[1].right and curr[1].left:
                        q.append((curr[1].left, curr[1].right))
                    elif curr[1].right:
                        q.append((curr[1].right, None))
                    elif curr[1].left:
                        q.append((curr[1].left, None))
                
        return root



