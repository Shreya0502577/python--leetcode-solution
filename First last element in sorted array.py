class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
          return [-1,-1]
        c,d=0,0
        for i in range(len(nums)):
         if nums[i]==target:
            c=i
            break
        for i in range(len(nums)-1,0,-1):
         if nums[i]==target:
            d=i
            break
        return [c,d] 