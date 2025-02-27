class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # need to do course schedule 1 first:
        # create an array of in-edges of length numCourses
        # and hashmap of prerequisites that adds all of the 
        # neighbors going into a node

        ans = []
        inedges = [0] * numCourses
        hmap = defaultdict(list)

        for prereq in prerequisites:
            inedges[prereq[0]] += 1
            hmap[prereq[1]].append(prereq[0])

        q = deque()
        for i in range(len(inedges)):
            if inedges[i] == 0:
                q.append(i)

        while q:
            currVal = q.popleft()
            ans.append(currVal)
            for nei in hmap[currVal]:
                inedges[nei] -= 1
                if inedges[nei] == 0:
                    q.append(nei)
        
        if len(ans) != numCourses:
            return []
        else:
            return ans
