class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        equal = 0
        less = 0
        for i in range(len(nums)):
            if nums[i] == target:
                equal += 1
            elif nums[i] < target:
                less += 1
        
        for i in range(equal):
            res.append(less)
            less += 1
        return res
         
   
         if nums[i]==target:
            c=i
            break
        for i in range(len(nums)-1,0,-1):
         if nums[i]==target:
            d=i
            break
        return [c,d] 