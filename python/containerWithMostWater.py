class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height)
        
        left = 0
        right = len(height) - 1
        current_max = 0
        
        while left < right:
            if height[left] > height[right]:
                current_max = max(current_max, height[right] * (right - left))
                right -= 1
            else:
                current_max = max(current_max, height[left] * (right - left))
                left += 1
                
        return current_max
            
