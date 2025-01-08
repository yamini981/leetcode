# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:


    # For serialization thinking to do in order traversal AND preorder traversal and then recreate 
    # the tree like that other LC problem? That seems easiest tbh...
    # i kinda forgot how to do that so good practice I guess lol
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        returnString = [""]

        def preOrderTraverse(root):
            if root == None:
                returnString[0] += "#,"
                return
            returnString[0] += str(root.val) + ","
            preOrderTraverse(root.left)
            preOrderTraverse(root.right)
        
        preOrderTraverse(root)
        return returnString[0]


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # For a node: there will always be 2 after saying left/right - if either is null then you're at the end
        # first value is left sub tree, second value is left left sub tree until "hashtag" then we go up. Next value would be
        # left right sub tree - needs to be some kind of DFS
        
        numArray = data.split(',')
        self.i = 0

        def dfs():
            if numArray[self.i] == "#":
                self.i += 1
                return None
            node = TreeNode(int(numArray[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        



            


        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))