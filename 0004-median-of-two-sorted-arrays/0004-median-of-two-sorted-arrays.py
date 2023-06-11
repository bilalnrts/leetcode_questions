class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mylist = nums1 + nums2
        mylist.sort()
        mid = len(mylist) // 2
        if (len(mylist) % 2 == 0):    
            return (float((mylist[mid] + mylist[mid - 1]) / 2))
        else:
            return (float(mylist[mid]))

                