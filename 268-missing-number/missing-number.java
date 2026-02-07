import java.util.HashSet;
import java.util.Set;

class Solution {
    public int missingNumber(int[] nums) {
        int n =nums.length;
        Set<Integer> set = new HashSet<>();
        for(int i:nums){
            set.add(i);
        }
        for(int i=0 ; i< n+1 ; i++){
            if(!set.contains(i)){
                return i;
            }
        }
        
        return -1;
        
    }
}