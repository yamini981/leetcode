class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # The actual algorithm is crazy i'm ngl 
        # this is inefficient
        # actual algo is "Knuth-Morris-Pratt Algo" lol

        while part in s:
            s = s.replace(part, "", 1)

        return s
