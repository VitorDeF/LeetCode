import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        int tamanho = nums.length;
        HashSet<Integer> setArray = new HashSet<Integer>();
        for(int i = 0 ; i < tamanho ; i++){
            if(setArray.contains(nums[i]))
                return true;
            setArray.add(nums[i]);
        }
        return false;
    }
}
