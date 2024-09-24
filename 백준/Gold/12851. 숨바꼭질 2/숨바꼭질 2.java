import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    static final int MAX = 100_001;
    static int[] arr = new int[MAX];

    static int n, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        n = temp[0];
        k = temp[1];

        if (n == k) {
            System.out.println(0);
            System.out.println(1);
        } else {
            int[] results = bfs(n);
            System.out.println(results[0]);
            System.out.println(results[1]);
        }
    }


    private static int[] bfs(int start) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{start, 0});
        int count = 0;
        int time = -1;

        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int currentX = temp[0];
            int currentTime = temp[1];

            if (currentX == k) {
                if (time == -1) {
                    time = currentTime;
                    count++;
                } else {
                    if (time == currentTime) {
                        count++;
                    }
                }
            }

            int nextTime = currentTime + 1;

            int[] dx = {currentX - 1, currentX + 1, currentX * 2};

            for (int i = 0; i < dx.length; i++) {
                int nextX = dx[i];

                if (canGo(nextX, nextTime)) {
                    arr[nextX] = nextTime;
                    queue.add(new int[]{nextX, nextTime});
                }
            }
        }

        return new int[]{time, count};
    }

    private static boolean overRange(int x) {
        return x < 0 || x >= MAX;
    }

    private static boolean canGo(int x, int currentTime) {
        if (overRange(x)) {
            return false;
        }

        // 처음이거나 처음이 아니지만 최소 시간과 현재 시간이 같은 경우
        if (arr[x] == 0 || arr[x] == currentTime) {
            return true;
        }
        return false;
    }

}