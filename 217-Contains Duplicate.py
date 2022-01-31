class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        contains = {}
        for num in nums:
            if num in contains:
                return True
            else:
                contains[num] = True
