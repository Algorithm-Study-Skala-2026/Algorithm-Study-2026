package wk04.jh.greedy.체육복;

import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        int[] clothes = new int[n];
        
        HashMap<Integer, Integer> hash = new HashMap<>();
        
        for(int i = 0; i < n; i++){
            clothes[i] = 1;
        }
        
        for(int i : lost){
            clothes[i - 1] = 0;
        }
        
        for(int i : reserve){
            clothes[i - 1] += 1;
        }
        
        for(int i = 0; i < n ; i++){
            if(clothes[i] == 0 && i - 1 >= 0 && clothes[i - 1] == 2){
                clothes[i - 1] = 1;
                clothes[i] = 1;
                answer++;
            }else if(clothes[i] == 0 && i + 1 < n && clothes[i + 1] == 2){
                clothes[i + 1] = 1;
                clothes[i] = 1;
                answer++;
            }else if(clothes[i] == 1 || clothes[i] == 2){
                answer++;
            }
        }
        
        return answer;
    }
}