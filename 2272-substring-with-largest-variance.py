class Solution:
    def largestVariance(self, s: str) -> int:
        # brute force would be check every sub string and calculate its
        # variance - O(n) to calculate variance, and O(n^2) sub strings so
        # O(n^3)

        # yoinked this solution from editorial... very hard

        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        globalMax = 0

        # go through all character pairs
        for i in range(26):
            for j in range(26):
                if i == j or counts[i] == 0 or counts[j] == 0:
                    continue

                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                major_count = 0
                minor_count = 0

                rest_minor = counts[j]

                for char in s:
                    if char == major:
                        major_count += 1
                    if char == minor:
                        minor_count += 1
                        rest_minor -= 1

                    if minor_count > 0:
                        globalMax = max(globalMax, major_count - minor_count)
                    
                    if major_count < minor_count and rest_minor > 0:
                        major_count = 0
                        minor_count = 0

        return globalMax