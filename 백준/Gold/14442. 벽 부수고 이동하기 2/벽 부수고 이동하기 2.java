import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static final int NOT_GO = 1;
    static final int GO = 0;

    static int n, m, k;
    static int[][] arr;

    static Queue<int[]> queue = new LinkedList<>();
    static int[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        k = Integer.parseInt(input[2]);

        arr = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j) - '0';
                visited[i][j] = Integer.MAX_VALUE;
            }
        }

        queue.add(new int[]{0, 0, 0, 1}); // y, x, 부순 벽 수, 이동 횟수
        visited[0][0] = 0;

        int result = bfs();
        System.out.println(result);
    }

    private static int bfs() {
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int y = current[0], x = current[1], broken = current[2], count = current[3];

            if (y == n - 1 && x == m - 1) {
                return count;
            }

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;

                if (arr[ny][nx] == GO) {
                    if (visited[ny][nx] > broken) {
                        visited[ny][nx] = broken;
                        queue.add(new int[]{ny, nx, broken, count + 1});
                    }
                } else if (arr[ny][nx] == NOT_GO && broken < k) {
                    if (visited[ny][nx] > broken + 1) {
                        visited[ny][nx] = broken + 1;
                        queue.add(new int[]{ny, nx, broken + 1, count + 1});
                    }
                }
            }
        }

        return -1;
    }
}