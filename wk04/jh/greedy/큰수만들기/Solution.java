package wk04.jh.greedy.큰수만들기;

import java.util.*;

class Solution {
    public String solution(String number, int k) {
        
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : number.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peekLast() < c) {
                stack.pollLast();
                k--;
            }
            stack.addLast(c);
        }
        while (k-- > 0) stack.pollLast();
        
        String answer = "";
        
        for(char c : stack){
            answer += c;
        }

        return answer;
    }
}