package wk02.JH.stack&queue.다리를지나는트럭;

import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new ArrayDeque<>();
        int currentWeight = 0;
        int index = 0;
        
        for(int i = 0; i < bridge_length; i++){
            bridge.add(0);
        }
        
        while (!bridge.isEmpty()) {
            answer++;
            
            currentWeight -= bridge.poll();

            if (index < truck_weights.length) {
                if (currentWeight + truck_weights[index] <= weight) {
                    bridge.add(truck_weights[index]);
                    currentWeight += truck_weights[index];
                    index++;
                } else {
                    bridge.add(0);
                }
            }
        }
                
        return answer;
    }
}