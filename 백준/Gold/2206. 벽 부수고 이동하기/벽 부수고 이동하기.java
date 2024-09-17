import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static final int NOT_GO = 1;
    static final int GO = 0;

    static final int[] START = {0, 0};
    static int[] END;

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0};

    static int n;
    static int m;

    static int[][] arr;
    static boolean[][][] isVisited;
    static Queue<int[]> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        n = temp[0];
        m = temp[1];

        arr = new int[n][m];
        isVisited = new boolean[2][n][m]; // 벽을 부순 경험 여부(1 : 있음, 0 : 없음)
        END = new int[]{n - 1, m - 1};

        // 초기화
        for (int i = 0; i < n; i++) {
            arr[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }

        int result = bfs();
        System.out.println(result);
    }

    private static int bfs() {
        int x = START[0];
        int y = START[1];

        queue.add(new int[]{y, x, 0, 1}); // y, x, 벽을 부순 경험 여부(1 : 있음, 0 : 없음)
        isVisited[0][y][x] = true;

        while (!queue.isEmpty()) {
            int[] t = queue.remove();
            int currentY = t[0];
            int currentX = t[1];
            int currentIsBrokenWall = t[2];
            int temp = t[3];

            if (isEnd(currentY, currentX)) {
                return temp;
            }

            for (int i = 0; i < 4; i++) {
                int ny = currentY + dy[i];
                int nx = currentX + dx[i];

                // 벽이 아닐 때
                if (canGoWhenNotWall(ny, nx, arr, currentIsBrokenWall)) {
                    // 이전에 벽을 부순 경험 여부에 따라서 방문 처리
                    // 벽을 부수고 와서 최단 거리이든
                    // 벽을 부수지 않고 최단 거리이든
                    // 두 가지 케이스의 최단 거리를 업데이트 한다.
                    isVisited[currentIsBrokenWall][ny][nx] = true;
                    queue.add(new int[]{ny, nx, currentIsBrokenWall, temp +1});
                }

                // 벽 일때
                if(canGoWhenWall(ny, nx, arr, currentIsBrokenWall)) {
                    isVisited[1][ny][nx] = true;
                    arr[ny][nx] = temp + 1;
                    queue.add(new int[]{ny, nx, 1, temp+1});
                }
            }
        }

        return -1;
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < n && x >= 0 && x < m;
    }

    private static boolean isEnd(int y, int x) {
        return y == END[0] && x == END[1];
    }

    // 벽이 아닐 때
    private static boolean canGoWhenNotWall(int y, int x, int[][] arr, int currentIsBrokenWall) {
        return isRange(y, x) && arr[y][x] == GO && !isVisited[currentIsBrokenWall][y][x];
    }

    // 벽일 때
    private static boolean canGoWhenWall(int y, int x, int[][] arr, int currentIsBrokenWall) {
        return isRange(y, x) && arr[y][x] == NOT_GO && currentIsBrokenWall == 0 && !isVisited[1][y][x];
    }
}