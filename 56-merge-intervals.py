class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # could make copy if necessary
        intervals.sort() 

        ans = []

        # make a copy
        currInterval = [intervals[0][0], intervals[0][1]]
        ans.append(currInterval)

        for start, end in intervals[1:]:
            if start <= currInterval[1] and currInterval[1] >= end:
                # do nothing - you're already encapsulated
                continue
            elif start <= currInterval[1]:
                currInterval[1] = end
            else:
                currInterval = [start, end]
                ans.append(currInterval)

        return ans



