class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            return ""
        
        if numRows == 1:
            return s
        
        i = 0
        max_i = len(s) - 1
        output = {}
        col = 0
        while i <= max_i:
            remainder = col % numRows
            if remainder == 0 or remainder == numRows - 1:  
                for j in range(numRows):
                    if i > max_i:
                        break
                    if j in output:
                        output[j].append(s[i])
                    else:
                        output[j] = [s[i]]
                    i += 1
                col = 0
            else:
                index = numRows - remainder - 1
                output[index].append(s[i])
                i += 1
            col += 1
        new_s = ""
        for key in output:
            for c in output[key]:
                new_s += c
        return new_s