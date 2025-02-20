class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # slow way: calculate min manhattan distance for every point vs. every point O(n^2)
        # ^^ that doesn't work
        # this is some graph theory shit that I am unfamiliar with 
        N = len(points)
        adj = defaultdict(list)

        # create adjacency list
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        visited = set()
        totalCost = 0
        minHeap = [(0, 0)] # cost, point
        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            totalCost += cost
            visited.add(i)
            for neighborCost, neighbor in adj[i]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (neighborCost, neighbor))
            
        return totalCost
