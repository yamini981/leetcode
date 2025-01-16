class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # this is going to be a logic trick with what XOR is...
        # O(n*m) solution is obvious - can literally just do the xor calculations
        # nums1[0] ^ nums2[0] ^ nums1[0] ^ nums2[1] ^ nums1[1] ^ nums2[0] ^ nums1[1] ^ nums2[1]
        # xor with yourself is 0
        # 0 ^ n = n
        res = 0
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return res
        elif len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
            # since nums1 and nums2 are odd, we can just xor every value in each array to get the ans
            for val in nums2:
                res ^= val
            for val in nums1:
                res ^= val
            return res
        elif len(nums1) % 2 == 1:
            # since nums1 is odd and nums2 is even, that means we can just xor everything in nums2
            for val in nums2:
                res ^= val
            return res
        else:
            # since nums2 is odd, that means we can just xor everything in nums1
            for val in nums1:
                res ^= val
            return res