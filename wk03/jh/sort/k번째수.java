package wk03.jh.sort.k번쨰수;

import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int n = commands.length;
        int[] answer = new int[n];
        for(int a = 0; a < n; a++){
            int i = commands[a][0];
            int j = commands[a][1];
            int k = commands[a][2];
            int len = j - i + 1;
            int[] temp = new int[len];
            if(i == j){
                answer[a] = array[i - 1];
            }else{
                int idx = 0;
                for(int b = i - 1; b < j; b++){
                    temp[idx] = array[b];
                    idx++;
                }
                Arrays.sort(temp);
                answer[a] = temp[k - 1];
            }
        }
        return answer;
    }
}