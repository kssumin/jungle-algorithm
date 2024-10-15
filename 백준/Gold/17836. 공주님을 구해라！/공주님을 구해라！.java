import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    static final int CAN_GO = 0;
    static final int WALL = 1;
    static final int GRAM = 2;

    static final int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static int n, m, t;
    static int[][] arr;
    static boolean[][][] isVisited;
    static Queue<int[]> queue = new LinkedList<>();
    static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = temp[0];
        m = temp[1];
        t = temp[2];
        arr = new int[n][m];
        isVisited = new boolean[n][m][2];

        for (int i = 0; i < n; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        int result = execute();

        if (result == -1) {
            System.out.println("Fail");
        } else {
            System.out.println(result);
        }
    }


    // 바이러스 활성시키기
    private static int execute() {
        queue.add(new int[]{0, 0, 0, 0});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int curY = cur[0];
            int curX = cur[1];
            int curTime = cur[2];
            int hasGram = cur[3];

            if (curTime > t) {
                continue;
            }

            if (curY == n - 1 && curX == m - 1) {
                return curTime;
            }

            for (int i = 0; i < 4; i++) {
                int nextY = curY + d[i][0];
                int nextX = curX + d[i][1];

                if (notRange(nextY, nextX)) {
                    continue;
                }

                if (isVisited[nextY][nextX][hasGram]) {
                    continue;
                }

                if (arr[nextY][nextX] == WALL && hasGram == 1) {
                    queue.add(new int[]{nextY, nextX, curTime + 1, hasGram});
                    isVisited[nextY][nextX][hasGram] = true;
                }

                if (arr[nextY][nextX] == GRAM) {
                    queue.add(new int[]{nextY, nextX, curTime + 1, 1});
                }

                if (arr[nextY][nextX] == CAN_GO) {
                    queue.add(new int[]{nextY, nextX, curTime + 1, hasGram});
                    isVisited[nextY][nextX][hasGram] = true;
                }
            }
        }
        return -1;
    }

    private static boolean notRange(int y, int x) {
        return y < 0 || y >= n || x < 0 || x >= m;
    }
}
