class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        holder = {}
        counter = 0
        i = 0
        i_max = len(nums1)
        j = 0
        j_max = len(nums2)
        num1 = 0
        num2 = 0
        
        if i_max == 0:
            num1 = float('Inf')
        else:
            num1 = nums1[0]
        if j_max == 0:
            num2 = float('Inf')
        else:
            num2 = nums2[0]
        
        while 1:
            if num1 == float('Inf') and num2 == float('Inf'):
                break
            elif num1 <= num2:
                holder[counter] = num1
                counter +=1
                if i < i_max - 1:
                    i += 1
                    num1 = nums1[i]
                else:
                    num1 = float('Inf')
            elif num2 < num1:
                holder[counter] = num2
                counter +=1
                if j < j_max - 1:
                    j += 1
                    num2 = nums2[j]
                else:
                    num2 = float('Inf')

        if len(holder) % 2 == 0:
            return (float(holder[len(holder) // 2] + holder[(len(holder) - 1) // 2])) / 2
        else:
            return holder[len(holder) // 2]
