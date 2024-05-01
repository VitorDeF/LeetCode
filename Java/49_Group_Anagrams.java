import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Integer, List<String>> map = new HashMap<>();
        Integer[] indice;
        char[] charArray;
        for(String s: strs){
            indice = new Integer[26];
            Arrays.fill(indice, 0);
            charArray = s.toCharArray();
            for(char c : charArray)
                indice[c - 'a'] += 1;
            if(!map.containsKey(Arrays.hashCode(indice)))
                map.put(Arrays.hashCode(indice), new ArrayList<>());
            map.get(Arrays.hashCode(indice)).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
