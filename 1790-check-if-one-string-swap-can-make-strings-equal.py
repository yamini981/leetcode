class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # doesn't matter which string we're changing -
        # both strings need to have the same number of characters
        

        diffCharPairs = []

        if len(s1) != len(s2):
            return False
        #bank kanb
        # b k, k b
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffCharPairs.append((s1[i], s2[i]))
            if len(diffCharPairs) > 2:
                return False
        if len(diffCharPairs) == 0:
            return True
        if len(diffCharPairs) == 1:
            return False

        return diffCharPairs[0][1] == diffCharPairs[1][0] and diffCharPairs[0][0] == diffCharPairs[1][1]
