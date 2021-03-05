#TimeComplexity:O(mlogm+nlogn) 
#SpaceComplexity: O(1)
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : No
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #For reduced space use sorting
        nums1.sort()
        nums2.sort()
        m=len(nums1);n=len(nums2)
        i=0;j=0;output=[]
        while(i<m and j<n):
            if nums1[i]==nums2[j]:
                output.append(nums1[i])
                i+=1;j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return output
        
        
        '''O(N) Space and O(m+n) Time
        #using Hashmap
        output=[]
        m=len(nums1);n=len(nums2) 
        dict1=Counter(nums1) #creating dict for count
        for i in nums2:
            if i in dict1:
                output.append(i)
                dict1[i]-=1
                if dict1[i]==0:
                    dict1.pop(i)
        return output        
        '''

                
        
        
        