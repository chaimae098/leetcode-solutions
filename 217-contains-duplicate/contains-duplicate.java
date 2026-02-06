import java.util.HashSet;
import java.util.Set;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for(int i :nums){
            if(!seen.add(i)){
                return true;
            }
        }
        return false;
    }
}