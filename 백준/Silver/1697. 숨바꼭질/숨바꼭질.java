

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    private static int k;
    private static boolean[] isVisited;
    private static final int LIMIT = 100002;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int n = temp[0];
        k = temp[1];
        isVisited = new boolean[LIMIT];

        System.out.println(bfs(n, 0));
    }

    private static int bfs(int current, int count) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{current, count});
        isVisited[current] = true;

        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int target = temp[0];
            int total = temp[1];

            if (target == k) {
                return total;
            }

            if (isRange(target * 2) && !isVisited[target*2]) {
                queue.add(new int[]{target * 2, total + 1});
                isVisited[target * 2] = true;
            }

            if (isRange(target - 1)&& !isVisited[target-1]) {
                queue.add(new int[]{target - 1, total + 1});
                isVisited[target-1] = true;
            }

            if (isRange(target + 1) && !isVisited[target+1]) {
                queue.add(new int[]{target + 1, total + 1});
                isVisited[target+1] = true;
            }
        }
        return -1;
    }

    private static boolean isRange(int current) {
        return 0 <= current && current < LIMIT;
    }
}