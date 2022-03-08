class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def solve(l, h):
            if l > h:
                return
            if l == h:
                return nums[l]
            mid = l + (h - l)//2
            if nums[mid] == nums[mid-1]:
                if (mid-l) % 2 == 0:
                    return solve(l, mid)
                else:
                    return solve(mid+1, h)
            elif nums[mid] == nums[mid+1]:
                if (h-mid) % 2 == 0:
                    return solve(mid, h)
                else:
                    return solve(l, mid-1)
            else:
                return nums[mid]
       
        return solve(0, len(nums)-1)
         
   
         if nums[i]==target:
            c=i
            break
        for i in range(len(nums)-1,0,-1):
         if nums[i]==target:
            d=i
            break
        return [c,d] 