class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(1,len(nums)):
            for y in range(1,len(nums)):
                if nums[y] < nums[y-1]:
                    nums[y],nums[y-1] = nums[y-1],nums[y]
        return nums