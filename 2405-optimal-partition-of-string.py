class Solution:
    def partitionString(self, s: str) -> int:
        # O(n) time #O(26) space
        count = 1
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                count += 1
                visited = set()
            visited.add(s[i])
        return count