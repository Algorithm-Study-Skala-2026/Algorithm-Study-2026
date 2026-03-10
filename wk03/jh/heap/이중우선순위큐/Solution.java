package wk03.jh.heap.이중우선순위큐;

import java.util.*;

class Solution {
    public int[] solution(String[] operations) {        
        TreeMap<Integer, Integer> pq = new TreeMap<>();
        
        for(String s : operations){
            String[] command = s.split(" ");
            int key;
            if(command[0].equals("I")){
                key = Integer.parseInt(command[1]);
                pq.put(key, pq.getOrDefault(key, 0) + 1);
            }else{
                if(pq.isEmpty()) continue;
                int val;
                if(command[1].equals("1")){
                    key = pq.lastKey();
                    int cnt = pq.get(key);
                    if (cnt == 1) pq.remove(key);
                    else pq.put(key, cnt - 1);
                }else{
                    key = pq.firstKey();
                    int cnt = pq.get(key);
                    if (cnt == 1) pq.remove(key);
                    else pq.put(key, cnt - 1);
                }
            }
        }
        
        if (pq.isEmpty()) return new int[]{0, 0};
        return new int[]{pq.lastKey(), pq.firstKey()};
    }
}