import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    static int n, k;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        n = temp[0];
        k = temp[1];

        arr = new int[100_001];

        int result = bfs(n);
        System.out.println(result);
    }

    private static int bfs(int start) {
        Queue<int[]> queue = new LinkedList<>();

        queue.add(new int[]{start, 0});
        arr[start] = 0;

        while (!queue.isEmpty()) {
            int[] temp = queue.remove();
            int x = temp[0];
            int time = temp[1];

            int nextTime = time + 1;

            if (x == k) {
                return time;
            }

            if (canGo(2 * x)) {
                arr[2 * x] = time;
                queue.add(new int[]{2 * x, time});
            }

            if (canGo(x - 1)) {
                arr[x - 1] = nextTime;
                queue.add(new int[]{x - 1, nextTime});
            }
            if (canGo(x + 1)) {
                arr[x + 1] = nextTime;
                queue.add(new int[]{x + 1, nextTime});
            }


        }
        throw new IllegalArgumentException("동생을 찾지 못한다.");
    }

    private static boolean isRange(int x) {
        return x >= 0 && x < 100_001;
    }

    private static boolean canGo(int x) {
        return isRange(x) && arr[x] == 0;
    }
}