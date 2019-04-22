from copy import deepcopy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []

        if (len(nums) == 0):
            return []

        if (len(nums) == 1):
            return [nums]   
        
        if (len(nums) == 2):
            nums2 = [nums[1], nums[0]]
            numsResult = [nums, nums2]
            return numsResult        
        
        output = []
        for num in nums:
            
            combinations = deepcopy(nums)
            combinations.remove(num)
            combinations = self.permute(combinations)
            
            for combination in combinations:
                output.append([num] + combination)
                
        return output

test1 = ([1,2,3])
print(Solution().permute(test1))