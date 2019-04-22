class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        
        output = []
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                output.append([candidate])
            elif candidate < target:
                results = self.combinationSum(candidates[i:], target - candidate)
                for result in results:
                    output.append([candidate] + result)
        return output
    
    

test1 = ([2,3,6,7], 7)
print(Solution().combinationSum(test1[0], test1[1]))
# [[2, 2, 3], [7]]

test2 = ([2,3,5], 8)
print(Solution().combinationSum(test2[0], test2[1]))
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

test3 = ([1], 2)
print(Solution().combinationSum(test3[0], test3[1]))
# [[1, 1]]

test4 = ([8,7,4,3], 11)
print(Solution().combinationSum(test4[0], test4[1]))
# [[3,4,4],[3,8],[4,7]]