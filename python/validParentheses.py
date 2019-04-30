class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        if len(s) == 1:
            return False
        
        brackets = ""
        
        for c in s:
            if c == "(" or c == "{" or c == "[":
                brackets += c
            else:
                if len(brackets) == 0:
                    return False
                elif c == ")" and brackets[-1] != "(":
                    return False
                elif c == "}" and brackets[-1] != "{":
                    return False
                elif c == "]" and brackets[-1] != "[":
                    return False
                brackets = brackets[:-1]
                
        if len(brackets) > 0:
            return False
        
        return True