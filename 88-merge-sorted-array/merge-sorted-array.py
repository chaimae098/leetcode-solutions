class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3=[]
        for i in range(m):
            nums3.append(nums1[i])
        k= len(nums3)    
        for j in range(n):
            nums3.append(nums2[j])
        for i in range(k+n-1):
          for j in range(0,n+k - i - 1) :
             if nums3[j]>nums3[j+1]:
                 nums3[j],nums3[j+1]=nums3[j+1],nums3[j]
        for i in range(n+k):
            nums1[i]=nums3[i]        
       


        