# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()

        def dfsInit(node, parent, isLeft):
            if node == None:
                return
            if parent == None:
                node.val = 0
            elif isLeft:
                node.val = 2 * parent.val + 1
            else:
                node.val = 2 * parent.val + 2
            self.values.add(node.val)

            dfsInit(node.left, node, True)
            dfsInit(node.right, node, False)

        dfsInit(self.root, None, None)
                


        # in this func, we just need to uncontaminate the binary tree

    def find(self, target: int) -> bool:
        # this self.values set is not necessary, but allows for O(1) time
        # with just a bit of extra space
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)