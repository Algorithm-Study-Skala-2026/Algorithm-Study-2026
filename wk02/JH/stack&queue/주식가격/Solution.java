package wk02.JH/stack&queue.주식가격;

import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        
        int n = prices.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i < n; i++){
            int cnt = 0;
            for(int j = i + 1; j < n; j++){
                if(prices[i] > prices[j]){
                    cnt += 1;
                    break;
                }else{
                    cnt += 1;
                }
            }
            stack.push(cnt);
        }
        
        for(int i = 0; i < n; i++){
            answer[n - i - 1] = stack.pop();
        }
        return answer;
    }
}
