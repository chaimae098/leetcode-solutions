import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n =nums.length;
        List<Integer> result = new ArrayList<>();
        Set<Integer> temp = new HashSet<>();
        for(int num :nums){
            temp.add(num);
        }
        for(int i=1 ; i<=n ; i++){
            if(!temp.contains(i)){
                result.add(i);
            }

        }
        return result;
        
    }
}