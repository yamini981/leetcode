class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        startTimings = sorted(intervals, key=lambda x: x[0])
        endTimings = sorted(intervals, key=lambda x: x[1])

        endPointer = 0

        numTakenRooms = 0
        for startPointer in range(len(intervals)):
            startTime = startTimings[startPointer][0]
            endTime = endTimings[endPointer][1]

            if startTime >= endTime:
                endPointer += 1
                numTakenRooms -= 1
            
            numTakenRooms += 1
        return numTakenRooms
            
