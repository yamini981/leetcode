class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # main problem seems to be shifting around the values in nums1
        # I think I can just loop through values in both
        # basic solution would be worst case O(m * n)
        # loop through all nums2 values and figure out 
        # which index they should be placed after
        # so a pair like 3: 1

        # O( m + n) time and O(m) space would just be use a new array

        i, j, c = m - 1, n - 1, len(nums1) - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[c] = nums1[i]
                i -= 1
            else:
                nums1[c] = nums2[j]
                j -= 1
            c -= 1
        while j >= 0:
            nums1[c] = nums2[j]
            j -= 1
            c -= 1
            

        
            