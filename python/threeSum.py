class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            num = nums[i]
            if i > 0 and num == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                lnum = nums[left]
                rnum = nums[right]
                total = num + lnum + rnum
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    output.append([num, lnum, rnum])
                    while left < right and lnum == nums[left + 1]:
                        left += 1
                    while left < right and rnum == nums[right - 1]:
                        right -= 1                     
                    left += 1
                    right -= 1
                
        return output
    
test = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(test))

test = [0, 0, 0, 0]
print(Solution().threeSum(test))

test = [-1,0,1,2,-1,-4]
print(Solution().threeSum(test))

test = [-2,0,0,2,2]
print(Solution().threeSum(test))