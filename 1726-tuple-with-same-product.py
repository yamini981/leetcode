class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # brute force seems easy - just O(n^4) tho lol
        # note - if we have a * b = c * d we also have:
        # a * b = d * c, b * a = c * d, b * a = d * c
        # numbers are distinct as well... 
        total = 0

        products = {}

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                products[nums[i] * nums[j]] = products.get(nums[i] * nums[j], 0) + 1

        for _, count in products.items():
            numPairs = (count - 1) * count // 2

            total += 8 * numPairs

        return total