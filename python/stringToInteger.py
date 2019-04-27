class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def isInt(s):
            try:
                int(s)
                return True
            except:
                return False
            
        def returnNum(num, isNegative):
            if isNegative == True:
                num = num * -1
            if num > 2147483647:
                return 2147483647
            elif num < -2147483647:
                return -2147483648
            else:
                return num            
            
        i = 0
        max_i = len(str) - 1
        isNegative = -1
        numStarted = False
        num = 0
        intType = type(0)
        
        while 1:
            if i > max_i:
                break
            c = str[i]
            if not numStarted:
                if c == " ":
                    i += 1
                elif c == "+":
                    if isNegative == -1:
                        i += 1
                        isNegative = False
                        numStarted = True 
                    else:
                        return 0
                elif c == "-":
                    if isNegative == -1:
                        i += 1                    
                        isNegative = True
                        numStarted = True 
                    else:
                        return 0
                elif isInt(c):
                    numStarted = True
                else:
                    return 0
            else:
                if isInt(c):
                    num = num * 10
                    num += int(c)
                    i += 1
                else:
                    return returnNum(num, isNegative)
        return returnNum(num, isNegative)      
                    
test = "-2"
print(Solution().myAtoi(test))