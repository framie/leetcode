class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n, n, res)
        return res
        
        
    def helper(self, left, right, res, s = ""):
        if right == 0 and left == 0:
            res.append(s)
        if left:
            self.helper(left - 1, right, res, s + "(")
        if right and right > left:
            self.helper(left, right - 1, res, s + ")")