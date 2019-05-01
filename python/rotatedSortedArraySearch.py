class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        return self.helper(nums, target, 0, len(nums) - 1)
    
    def helper(self, nums, target, left, right):
        if right < left:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= target < nums[mid]:
            return self.helper(nums, target, left, mid - 1)
        elif nums[mid] < target <= nums[right] or nums[mid] > nums[right]:
            return self.helper(nums, target, mid + 1, right)
        return self.helper(nums, target, left, mid - 1)
