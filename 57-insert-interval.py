class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        retIntervals = []
        newAdded = False
        newIntervalToAdd = [newInterval[0], newInterval[1]]
        for interval in intervals:
            if (newIntervalToAdd[0] > interval[1]):
                retIntervals.append(interval)
            elif newIntervalToAdd[1] < interval[0]:
                if not newAdded:
                    retIntervals.append(newIntervalToAdd)
                    newAdded = True
                retIntervals.append(interval)
            else:
                newIntervalToAdd[0] = min(interval[0], newIntervalToAdd[0])
                newIntervalToAdd[1] = max(interval[1], newIntervalToAdd[1])
            
        
        if not newAdded:
            retIntervals.append(newIntervalToAdd)

        return retIntervals
            