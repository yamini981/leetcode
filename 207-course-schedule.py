class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph problem - you have a bunch of prerequisites
        # Editorial explains the algo very well
        # essentially, keep track of each node and its neighbors
        # as well as the number of edges going into that node 
        # Add all of the nodes that don't have any incoming edges
        # to a queue and run BFS. Each time you pop the queue, increment
        # a variable that tracks the number of nodes visited
        # For each neighbor of your popped node decrement
        # the number of incoming edges since it's been used
        # and if that node now has 0 incoming edges, add it to the queue
        # draw it out - makes a bunch of sense 
        # https://leetcode.com/problems/course-schedule/editorial
        adj = defaultdict(list)

        indegree = [0] * numCourses
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        nodesVisited = 0

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            currPoint = q.popleft()
            nodesVisited += 1
            for nei in adj[currPoint]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return nodesVisited == numCourses