class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # an array from 0 - 25 to track count of each stream
        hashmap = {}
        def getIndex(c):
            return ord(c) - ord('a')
        for s in strs:
            count = [0] * 26
            for char in s:
                count[getIndex(char)] += 1
            
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(s)
            else:
                hashmap[tuple(count)] = [s]
            
        return hashmap.values()
            

