class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)

        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
            valToFind = target - nums[i]
            if valToFind in hashmap:
                if valToFind == nums[i]:
                    if len(hashmap[valToFind]) == 2:
                        return [i, hashmap[valToFind][0]]
                else:
                    return [i, hashmap[valToFind][0]]