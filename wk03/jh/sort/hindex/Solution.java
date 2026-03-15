package wk03.jh.sort.hindex;

import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int answer = 0;

        for (int i = 0; i < n; i++) {
            int count = n - i;
            answer = Math.max(answer, Math.min(citations[i], count));
        }
        return answer;
    }
}
