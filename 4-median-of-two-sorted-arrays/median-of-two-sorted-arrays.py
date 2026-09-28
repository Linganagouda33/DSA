class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=sorted(nums1+nums2)
        n=len(nums)
        mid = n // 2
        if n%2==0:
            return (nums[mid-1]+nums[mid])/2.0
        else:
            return nums[mid]