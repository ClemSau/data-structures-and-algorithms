# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2 # merge the two arrays
        nums3.sort()
        length = len(nums3)
        if length % 2 == 1:
            return nums3[int(length/2 - 0.5)]
        else:
            return ((nums3[int(length/2 - 1)] + nums3[int(length/2)]) / 2)