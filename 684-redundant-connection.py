class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycleSet = set()
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycleSet.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False

        dfs (1, -1)
        for u, v in reversed(edges):
            if u in cycleSet and v in cycleSet:
                return [u, v]
        return []