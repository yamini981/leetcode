class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSum = [0] * len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        if words[0][0] in vowels and words[0][-1] in vowels:
            prefixSum[0] = 1

        for i in range(1, len(words)):
            prefixSum[i] = prefixSum[i-1]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefixSum[i] += 1
        
        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = prefixSum[queries[i][1]]
            if queries[i][0] != 0:
                ans[i] -= prefixSum[queries[i][0] - 1]

        return ans
