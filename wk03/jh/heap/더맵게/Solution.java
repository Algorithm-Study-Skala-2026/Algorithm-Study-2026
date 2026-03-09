package wk03.jh.heap.더맵게;

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) pq.add(s);

        int answer = 0;

        while (pq.size() >= 2 && pq.peek() < K) {
            int a = pq.poll();
            int b = pq.poll();
            pq.offer(a + b * 2);
            answer++;
        }

        return (pq.peek() != null && pq.peek() >= K) ? answer : -1;
    }
}
