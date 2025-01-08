class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # go through each array and 
        # get the max value (biggest of each last array)
        # also get the min value (smallest of each start array)
        # track second biggest and second smallest
        # if biggest and smallest are same index:
        # take max of (max - secondMin, secondMax - min)
        max1 = arrays[0][len(arrays[0]) - 1]
        max2 = arrays[1][len(arrays[1]) - 1]
        if max1 > max2:
            maxValue = (max1, 0)
            secondMax = (max2, 1)
        else:
            maxValue = (max2, 1)
            secondMax = (max1, 0)
        
        min1 = arrays[0][0]
        min2 = arrays[1][0]

        if min1 < min2:
            minValue = (min1, 0)
            secondMin = (min2, 1)
        else:
            minValue = (min2, 1)
            secondMin = (min1, 0)


        for i in range(2, len(arrays)):
            newMin = arrays[i][0]
            newMax = arrays[i][len(arrays[i]) - 1]
            
            if newMax > maxValue[0]:
                secondMax = maxValue
                maxValue = (newMax, i)
            elif newMax > secondMax[0]:
                secondMax = (newMax, i)
            if newMin < minValue[0]:
                secondMin = minValue
                minValue = (newMin, i)
            elif newMin<secondMin[0]:
                secondMin = (newMin, i)

        if maxValue[1] == minValue[1]:
            return max(maxValue[0] - secondMin[0], secondMax[0] - minValue[0])
        else:
            return maxValue[0] - minValue[0]
