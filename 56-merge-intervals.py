class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()
        currMerge = [intervals[0][0], intervals[0][1]]

        for i in range(1, len(intervals)):
            currInterval = intervals[i]

            if currMerge[1] >= currInterval[0]:
                currMerge[1] = max(currMerge[1], currInterval[1])
            else:
                res.append(currMerge)
                currMerge = [currInterval[0], currInterval[1]]

        res.append(currMerge)

        return res
