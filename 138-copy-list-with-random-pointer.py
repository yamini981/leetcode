"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. Create node to index dictioniary
        # 2. Create random to node index array
        # 3. Copy over standard linked list
        # 4. Create index to new node array
        # 5. Set the random values in new list based on the index to new node array
        if head == None:
            return None
        
        nodeToIndex = {}
        currNode = head
        index = 0
        while currNode:
            nodeToIndex[currNode] = index
            index += 1
            currNode = currNode.next
        numNodes = index

        randomIndices = [-1] * (numNodes)
        
        currNode = head
        while currNode:
            currIndex = nodeToIndex[currNode]
            if currNode.random:
                randIndex = nodeToIndex[currNode.random]
                randomIndices[currIndex] = randIndex
            currNode = currNode.next
        
        newNodeList = [None] * numNodes
        newHead = Node(head.val, None, None)

        newNodeList[0] = newHead

        currNode = head.next
        prevNewNode = newHead
        i = 1
        while currNode:
            newNode = Node(currNode.val, None, None)
            newNodeList[i] = newNode
            prevNewNode.next = newNode

            prevNewNode = newNode
            currNode = currNode.next
            i += 1

        for i in range(numNodes):
            currentRandomIndex = randomIndices[i]
            if currentRandomIndex != -1:
                newNodeList[i].random = newNodeList[randomIndices[i]]

        return newHead




        
