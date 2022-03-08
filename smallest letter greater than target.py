class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        l = 0
        r = len(letters)
        while l < r:
            m = l + (r - l) // 2
            
            if letters[m] <= target:
                
                l = m + 1
           
            else:
                
                r = m
        return letters[l]