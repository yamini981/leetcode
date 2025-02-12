class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # collect sum of digits and put into a hashmap with with their current values

        def calcSumDigits(number):
            total = 0
            while number > 0:
                total += number % 10
                number = number // 10

            return total
        
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[calcSumDigits(nums[i])].append(nums[i])
        
        bestSum = -1
        for _, val in hashmap.items():
            if len(val) >= 2:
                val.sort()
                bestSum = max(bestSum, val[-1] + val[-2])
        return bestSum
                
