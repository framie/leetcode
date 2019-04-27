class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        digit = 0
        is_negative = False
        i = 0

        if x < 0:
            is_negative = True
            x = x * -1

        while x != 0:
            digit = x % 10
            num = num * 10
            num = num + digit
            x = x - digit
            x = x // 10
            i = i + 1
            

        if is_negative:
            num = num * -1
            
        if num < -2147483648 or num > 2147483647:
            return 0

        return num