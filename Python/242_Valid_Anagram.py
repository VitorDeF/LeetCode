from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapaS, mapaT = defaultdict(int), defaultdict(int)
        
        for letter in s:
                mapaS[letter] += 1

        for letter in t:
                mapaT[letter] += 1

        return mapaS == mapaT