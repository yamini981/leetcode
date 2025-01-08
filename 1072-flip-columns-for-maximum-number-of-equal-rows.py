class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashmap = {}

        for row in matrix:
            first = row[0]
            canonical = ""
            for i in row:
                if i == first:
                    canonical += '1'
                else:
                    canonical += '0'
                
            hashmap[canonical] = hashmap.get(canonical, 0) + 1
            
        return max(0, max(hashmap.values()))