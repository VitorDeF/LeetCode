class Solution(object):
    def containsDuplicate(self, nums): 
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapa = set(nums)
        return len(mapa)!=len(nums)