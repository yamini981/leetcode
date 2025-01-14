class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0] * len(A)
        setA = {}
        setB = {}
        for i in range(len(A)):

            setA[A[i]] = setA.get(A[i], 0) + 1
            setB[B[i]] = setB.get(B[i], 0) + 1
            if i > 0:
                C[i] = C[i - 1]
            if A[i] == B[i]:
                C[i] += 1
            else:
                if A[i] in setB and setA[A[i]] <= setB[A[i]]:
                    C[i] += 1
                if B[i] in setA and setB[B[i]] <= setA[B[i]]:
                    C[i] += 1
        return C


