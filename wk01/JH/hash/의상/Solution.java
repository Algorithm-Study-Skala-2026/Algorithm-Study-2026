package wk01.JH.hash.의상;

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> hash = new HashMap<>();
        for (int i = 0; i < clothes.length; i++) {
            hash.put(clothes[i][1], hash.getOrDefault(clothes[i][1], 0) + 1);
        }

        int answer = 1;
        for (int cnt : hash.values()) {
            answer *= (cnt + 1);
        }

        return answer - 1;
    }
}
