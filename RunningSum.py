'''
1480. Running Sum of 1d Array
by Laith Kamal
'''

class Solution(object):
    def runningSum(self, nums):
        result = []
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            result.append(currentSum)
        return result



