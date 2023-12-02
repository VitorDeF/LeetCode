from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapa = defaultdict()
        for i,number in enumerate(nums):
            if target-number in mapa:
                return [mapa[target-number],i]
            mapa[number] = i