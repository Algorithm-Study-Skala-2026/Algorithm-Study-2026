import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int cnt = 0;

        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));

        HashMap<Integer, ArrayList<Integer>> hash = new HashMap<>();
        for (int i = 0; i < n; i++) {
            hash.put(i, new ArrayList<>());
        }

        for (int[] arr : costs) {
            int start = arr[0];
            int end = arr[1];
            int cost = arr[2];

            if (isConnected(start, end, hash, new boolean[n])) {
                continue;
            }

            hash.get(start).add(end);
            hash.get(end).add(start);
            answer += cost;
            cnt++;

            if (cnt == n - 1) break;
        }

        return answer;
    }

    private boolean isConnected(int start, int end, HashMap<Integer, ArrayList<Integer>> graph, boolean[] visited) {
        if (start == end) return true;

        visited[start] = true;

        for (int next : graph.get(start)) {
            if (!visited[next]) {
                if (isConnected(next, end, graph, visited)) {
                    return true;
                }
            }
        }

        return false;
    }
}
