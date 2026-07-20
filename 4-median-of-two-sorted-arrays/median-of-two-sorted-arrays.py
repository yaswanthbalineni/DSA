class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=sorted(nums1+nums2)
        n=len(m)
        if n%2==1:
            return m[n//2]
        else:
            return (m[n//2-1]+m[n//2])/2