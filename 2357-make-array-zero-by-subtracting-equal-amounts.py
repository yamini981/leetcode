class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # subtract as much as you can every time
        # if sorted seems very easy, but thats nlogn.
        # does seem like the answer might just be the number of 
        # unique numbers not including 0
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(num)
        
        if 0 in uniqueNums:
            return len(uniqueNums) - 1
        else:
            return len(uniqueNums)