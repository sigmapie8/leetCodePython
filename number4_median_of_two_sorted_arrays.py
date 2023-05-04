class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merged array
        nums3 = sorted(nums1 + nums2)

        # median
        totalCount = len(nums3)
        if(totalCount%2 == 1):
            return nums3[totalCount//2]
        else:
            return (nums3[(totalCount//2)-1] + nums3[totalCount//2])/2
