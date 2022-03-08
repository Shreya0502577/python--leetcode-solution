class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
       list1= nums[:n]
       list2 = nums[n:]
       return_list = []
       for i in range(0,len(list1)):
            return_list.append(list1[i])
            return_list.append(list2[i])
            
       return return_list
        