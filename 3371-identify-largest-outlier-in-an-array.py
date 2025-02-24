class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # so you have a bunch of numbers in an array
        # and they add up to another number in the array
        # maybe make prefix sums...? let's think that through

        prefix = [None] * len(nums)

        prefixMinusNums = collections.defaultdict(list)

        total = sum(nums)
        for k in range(len(nums)):
            prefix[k] = total - nums[k]
            prefixMinusNums[prefix[k] - nums[k]].append(k)
        maxOutlier = -1001
        for i, num in enumerate(nums):
            if num in prefixMinusNums:
                listToCheck = prefixMinusNums[num]
                if i == listToCheck[0]:
                    if len(listToCheck) >= 2:
                        maxOutlier = max(num, maxOutlier)
                else:
                    maxOutlier = max(num, maxOutlier)

        return maxOutlier


        