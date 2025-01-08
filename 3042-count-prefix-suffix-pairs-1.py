class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ret = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                str1 = words[i]
                str2 = words[j]
                if (len(str1) <= len(str2) and 
                    str1 == str2[:len(str1)] and 
                    str1 == str2[(len(str2) - len(str1)):]):
                    ret += 1 

        return ret
