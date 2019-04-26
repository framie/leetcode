class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        current = s[0]
        length = 1
        longest = 1
        for i in range(1, len(s)):
            c = s[i]
            if c not in current:
                current += c
                length += 1
                if length > longest:
                    longest = length
            else:
                current = current[current.find(c) + 1:] + c
                length = len(current)
                
        return longest
                