package stackqueue.같은숫자는싫어;

import java.util.*;

public class Solution {
    public int[] solution(int []arr) {        
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i < arr.length; i++){
            if(stack.isEmpty() || stack.peek() != arr[i])
                stack.add(arr[i]);
        }
        
        int len = stack.size();
        int[] answer = new int[len];

        for(int i = len - 1; i >= 0; i--){
            answer[i] = stack.pop();
        }
        return answer;
    }
}