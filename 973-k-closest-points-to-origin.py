class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # could create array of euclidean distances to origin that has the index of the point as well

        distances = [None] * len(points)

        for i in range(len(points)):
            euclid = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            distances[i] = (euclid, i)
        
        distances.sort()

        ans = [None] * k

        for i in range(k):
            ans[i] = points[distances[i][1]]

        return ans