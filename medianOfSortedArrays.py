#TimeComplexity:O(logn) where n is length of smallest array 
#SpaceComplexity: O(1)
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : No
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1);n=len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2,nums1)
        low=0;high=m
        while(low<=high):
            mid=low+(high-low)//2
            p1=mid
            p2=((m+n)//2)-p1
            l1=nums1[p1-1] if p1>0 else float('-inf')
            r1=nums1[p1] if p1<m else float('inf')
            l2=nums2[p2-1] if p2>0 else float('-inf')
            r2=nums2[p2] if p2<n else float('inf')
            
            if l1<=r2 and l2<=r1:
                #got answer
                print(l1,l2,r1,r2)
                if (m+n)%2==0:
                    return float((max(l1,l2)+min(r1,r2))/2)
                else:
                    return min(r1,r2)
            elif l1>r2:
                high=mid-1
            else:
                low=mid+1
        
        
        