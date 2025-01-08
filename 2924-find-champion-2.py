class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weakSet = set()

        for edge in edges:
            weak = edge[1]
            strong = edge[0]
            weakSet.add(weak)

        if len(weakSet) == n or len(weakSet) <= n - 2:
            return -1


        for i in range(n):
            if i not in weakSet:
                return i