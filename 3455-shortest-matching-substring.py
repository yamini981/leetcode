class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # * can become ANY sequence of characters
        # if there were no *'s, we could just use sliding window
        # if there was 1 *, we could do some weird sliding window shit but it would work
        # with 2 *'s i'm kinda fucked

        # split up p into 3 segments
        pSegs = ['', '', '']
        segNum = 0
        for i in range(len(p)):
            if p[i] == "*":
                segNum += 1
                continue
            pSegs[segNum] += p[i]
        pSegLen = len(pSegs[0]) + len(pSegs[1]) + len(pSegs[2])
        a = pSegs[0]
        b = pSegs[1]
        c = pSegs[2]

        minLen = float('inf')

        def findSubStringIndices(substring):
            ans = []
            # start = s.find(substring, 0)
            # while start != -1:
            #     ans.append(start)
            #     start = s.find(substring, start)
            #     start += len(substring)
            if len(substring) == 0:
                return []
            start = 0
            while True:
                start = s.find(substring, start)
                if start == -1:
                    break
                ans.append(start)
                start += 1
            return ans
        
        aIndices = findSubStringIndices(a)
        bIndices = findSubStringIndices(b)
        cIndices = findSubStringIndices(c)

        # need lowest value that is bigger than target
        def binarySearch(array, target):
            l, r = 0, len(array) - 1
            while l <= r:
                mid = (r + l) // 2
                if array[mid] == target:
                    return array[mid]
                elif array[mid] < target:
                    l = mid + 1
                elif array[mid] > target:
                    oldR = r
                    r = mid
                    if r == oldR:
                        return array[r]
            return -1
        minLen = float('inf')
        if len(a) == 0 and len(b) == 0 and len(c) == 0:
            return 0
        elif ((len(a) == 0 and len(b) == 0)
            or (len(b) == 0 and len(c) == 0)
            or (len(a) == 0 and len(c) == 0)):
            return pSegLen
        elif len(a) == 0:
            for bIndex in bIndices:
                cIndex = binarySearch(cIndices, bIndex + len(b))
                if cIndex == -1:
                    continue
                minLen = min(minLen, pSegLen + cIndex - bIndex - len(b))
        elif len(b) == 0:
            for aIndex in aIndices:
                cIndex = binarySearch(cIndices, aIndex + len(a))
                if cIndex == -1:
                    continue
                minLen = min(minLen, pSegLen + cIndex - aIndex - len(a))
        elif len(c) == 0:
            for aIndex in aIndices:
                bIndex = binarySearch(bIndices, aIndex + len(a))
                if bIndex == -1:
                    continue
                minLen = min(minLen, pSegLen + bIndex - aIndex - len(a))
        else:
            for aIndex in aIndices:
                bIndex = binarySearch(bIndices, aIndex + len(a))
                
                if bIndex == -1:
                    continue
                distance = bIndex - aIndex - len(a)
                cIndex = binarySearch(cIndices, bIndex + len(b))
                if cIndex == -1:
                    continue
                distance += cIndex - bIndex - len(b)
                minLen = min(minLen, pSegLen + distance)
        if minLen == float('inf'):
            return -1
        else:
            return minLen


        

        # for i in range(len(s)):
        #     window1 = s[i:i + len(pSegs[0])]
        #     if window1 == pSegs[0]:
        #         numChars = 0
        #         if len(pSegs[1]) == 0 and len(pSegs[2]) == 0:
        #             return pSegLen
        #         for j in range(i + len(pSegs[0]), len(s)):
        #             window2 = s[j : j + len(pSegs[1])]
        #             if window2 == pSegs[1]:
        #                 if len(pSegs[2]) == 0:
        #                     minLen = min(pSegLen + numChars, minLen)
        #                     continue
        #                 for k in range(j + len(pSegs[1]), len(s)):
        #                     window3 = s[k : k + len(pSegs[2])]
        #                     if window3 == pSegs[2]:
        #                         minLen = min(pSegLen + numChars, minLen)
        #                     numChars += 1
        #             numChars += 1
        # if minLen == float('inf'):
        #     return -1
        # else:
        #     return minLen
            