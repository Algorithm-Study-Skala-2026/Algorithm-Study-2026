package wk02.JH.stack&queue.프로세스;

import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        Queue<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < priorities.length; i++){
            queue.add(priorities[i]);
        }
        
        while(true){
            int max = Collections.max(queue);
            int temp = queue.peek();
            if(temp == max){
                if(location == 0){
                    break;
                }else{
                    queue.poll();
                    location = changeLoc(location, queue.size());
                    answer++;
                }
            }else{
                queue.poll();
                queue.add(temp);
                location = changeLoc(location, queue.size());
            }
        }
        return answer;
    }
    
    private int changeLoc(int loc, int size){
        if(loc == 0) return size - 1;
        else return loc - 1;
    }
}