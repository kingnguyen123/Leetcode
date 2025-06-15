#give array, int k , int x
# return the array with size if n - k +1. And contain the x^th smallest number in each sub array
#waht is the relation ship between x smallest number with array?
from sortedcontainers import SortedList
class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        result=[]
        window = SortedList()
        # result.append(sorted(window[x-1]))
        for i in range(len(nums)):
            window.add(nums[i])
            if i >= k :
                window.remove(nums[i-k])
            if i>= k-1: # if we can reduce compute time of this phase.that would be perfect!!!
                val = window[x - 1]
                count=sum(1 for i in window if i <0)
                if count < x:
                    result.append(0)
                else:
                    result.append(val)

        return result

x=Solution()
print(x.getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1))
