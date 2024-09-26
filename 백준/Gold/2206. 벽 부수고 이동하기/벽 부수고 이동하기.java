import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 벽을 1개까지 부수는 것은 가능하다.
 */
public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static final int WALL = 1;
    static final int GO = 0;

    static final int NOT_BROKEN_WALL = 0;
    static final int BROKEN_WALL = 1;

    static int n, m, k;
    static int[][] arr;

    static Queue<int[]> queue = new LinkedList<>();
    static int[][] brokenCountArr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = temp[0];
        m = temp[1];
//        k = temp[2];
        k = 1;

        arr = new int[n][m];
        brokenCountArr = new int[n][m];

        for (int i = 0; i < n; i++) {
            arr[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }

        for (int[] ints : brokenCountArr) {
            Arrays.fill(ints, Integer.MAX_VALUE);
        }

        queue.add(new int[]{0, 0, NOT_BROKEN_WALL, 1}); // 현재 이동까지 벽을 부순 수, 이동 횟수
        brokenCountArr[0][0] = NOT_BROKEN_WALL;

        int result = bfs();
        System.out.println(result);
    }

    private static int bfs() {
        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int currentY = temp[0];
            int currentX = temp[1];
            int brokenCount = temp[2];
            int count = temp[3];

            if (currentY == n - 1 && currentX == m - 1) {
                return count;
            }

            for (int i = 0; i < 4; i++) {
                int nextY = currentY + dy[i];
                int nextX = currentX + dx[i];

                // 벽을 부수지 않는 케이스
                if (canGoNotWall(nextY, nextX, brokenCount)) {
                    queue.add(new int[]{nextY, nextX, brokenCount, count + 1});
                    brokenCountArr[nextY][nextX] = brokenCount;
                }
                // 벽을 부수는 케이스
                else if (canGoWithBrokenWall(nextY, nextX, brokenCount)) {
                    queue.add(new int[]{nextY, nextX, brokenCount + 1, count + 1});
                    brokenCountArr[nextY][nextX] = brokenCount + 1;
                }
            }
        }
        return -1;
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < n && x >= 0 && x < m;
    }

    private static boolean canGoNotWall(int y, int x, int brokenCount) {
        return isRange(y, x) && arr[y][x] == GO && brokenCountArr[y][x] > brokenCount; // 0이면 최초, 더 작은 횟수로 먼저 도착했다면 업데이트 안 해도 됌
    }

    private static boolean canGoWithBrokenWall(int y, int x, int brokenCount) {
        return isRange(y, x) && arr[y][x] == WALL && brokenCount + 1 <= k && brokenCountArr[y][x] > brokenCount + 1;
    }
}
