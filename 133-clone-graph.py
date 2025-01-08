"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        q = deque([node])
        
        cloneGraph = Node(node.val, None)
        created = {node : cloneGraph}
    
        while len(q) > 0:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in created:
                    q.append(neighbor)
                    cloneNeighbor = Node(neighbor.val, None)
                    created[neighbor] = cloneNeighbor
                    
                created[curr].neighbors.append(created[neighbor])
                    
        return cloneGraph
                




        