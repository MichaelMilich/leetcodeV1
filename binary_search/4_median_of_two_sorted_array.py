class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        n = len(nums1)
        m = len(nums2)
        k = n + m
        merge_half_idx = k // 2 - 1 if k % 2 == 0 else k // 2
        
        return 0
