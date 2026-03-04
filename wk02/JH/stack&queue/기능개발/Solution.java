import java.util.*;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new  ArrayDeque<>();

        int n = progresses.length;
        int[] days = new int[n];

        for(int i = 0; i < n; i++){
            days[i] = (int) Math.ceil((100 - progresses[i]) / (double) speeds[i]);
        }

        int cnt = 0;
        int max = days[0];

        for(int i = 0; i < n; i++){
            if(days[i] <= max){
                cnt++;
            } else {
                queue.add(cnt);
                cnt = 1;
                max = days[i];
            }
        }
        queue.add(cnt);
        int m = queue.size();
        int[] answer = new int[m];
        for(int i = 0;i < m; i++){
            answer[i] = queue.poll();
        }
        return answer;
    }
}
