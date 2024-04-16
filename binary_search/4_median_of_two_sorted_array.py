from statistics import median


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
        :param nums1:
        :param nums2:
        :return:
        """
        # todo: write the actual solution and not use magic functions :)
        return median(sorted(nums1+nums2))
