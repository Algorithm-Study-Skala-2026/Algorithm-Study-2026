package wk01.JH.hash.완주하지못한선수;

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hash = new HashMap<>();
        for(String s : completion){
            hash.put(s, hash.getOrDefault(s, 0) + 1);
        }
        for(String s : participant){
            if(hash.getOrDefault(s,0) == 0) return s;
            else hash.put(s, hash.get(s) - 1);
        }
        
        return "error";
    }
}