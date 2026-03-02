package wk01.JH.hash.폰켓몬;

import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i : nums){
            if(!list.contains(i)){
                list.add(i);
                answer++;
                if(answer == nums.length / 2)
                    break;
            }
        }
        
        return answer;
    }
}