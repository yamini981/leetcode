class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(list)

        for i, num in enumerate(nums):
            hmap[num].append(i)
        
        
        for i, num in enumerate(nums):
            if target - num in hmap:
                if target - num == num:
                    if len(hmap[target-num]) >= 2:
                        return [i, hmap[target-num][1]]
                    else:
                        continue
                else:
                    return [i, hmap[target-num][0]]
