package wk05.jh.greedy.단속카메라;

import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

        int camera = Integer.MIN_VALUE; 
        int answer = 0;

        for (int[] route : routes) {
            int start = route[0];
            int end = route[1];

            if (start > camera) {
                answer++;
                camera = end; 
            }
        }

        return answer;
    }
}