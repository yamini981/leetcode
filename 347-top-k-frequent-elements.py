class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        maxFreq = 0
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            maxFreq = max(hashmap[n], maxFreq)
        
        bucket = [[] for _ in range(maxFreq + 1)]
        for num, freq in hashmap.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return None