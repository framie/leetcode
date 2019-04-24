class Solution(object):
    def twoSum(self, nums, target):
        checked = dict()
        for i in range(len(nums)):
            current = nums[i]
            if current in checked:
                return [checked[current], i]
            else:
                checked[target - current] = i