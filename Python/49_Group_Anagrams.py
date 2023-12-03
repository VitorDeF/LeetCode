class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        listaOrdenada, listaFinal = list(), list()
        for string in strs:
            listaOrdenada.extend(sorted(string))
        for string in strs:
            if sorted(string) in listaOrdenada:
                listaFinal[listaOrdenada.index(sorted(string))]+=string
            else:
                listaFinal.append(list(string))
        return(listaFinal)