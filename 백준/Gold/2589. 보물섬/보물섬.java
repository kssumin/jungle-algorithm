import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    static int m, n; // m : 세로, n : 가로
    static int[][] arr;
    static Queue<int[]> queue = new LinkedList<>();
    static boolean[][] isVisited;

    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        m = temp[0];
        n = temp[1];

        arr = new int[m][n];

        // 초기화
        for (int i = 0; i < m; i++) {
            char[] line = br.readLine().toCharArray();

            for (int j = 0; j < n; j++) {
                if (line[j] == 'L') {
                    arr[i][j] = 0;
                } else {
                    arr[i][j] = -1;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == 0) {
                    int[][] copy = deepCopy(arr);
                    execute(i, j, copy);
                }
            }
        }

        System.out.println(result);
    }

    private static void execute(int i, int j, int arr[][]) {
        isVisited = new boolean[m][n];

        isVisited[i][j] = true;
        queue.add(new int[]{i, j});
        bfs(arr, isVisited);


        int max = findMax(arr);

        if (result < max) {
            result = max;
        }
    }

    private static void bfs(int[][] arr, boolean[][] isVisited) {
        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int y = temp[0];
            int x = temp[1];

            int target = arr[y][x];

            for (int i = 0; i < 4; i++) {
                int nextX = x + dx[i];
                int nextY = y + dy[i];

                if (canGo(nextY, nextX, arr, isVisited)) {
                    isVisited[nextY][nextX] = true;
                    arr[nextY][nextX] = target + 1;

                    queue.add(new int[]{nextY, nextX});
                }
            }
        }
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < m && x >= 0 && x < n;
    }

    private static boolean canGo(int y, int x, int[][] arr, boolean[][] isVisited) {
        return isRange(y, x) && arr[y][x] == 0 && !isVisited[y][x];
    }
    
    private static int findMax(int[][] arr) {
        int result = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int temp = arr[i][j];

                if (temp > result) {
                    result = temp;
                }
            }
        }

        return result;
    }

    private static int[][] deepCopy(int[][] origin) {
        int[][] copy = new int[m][n];

        for (int i = 0; i < m; i++) {
            copy[i] = Arrays.copyOf(origin[i], origin[i].length);
        }

        return copy;
    }
}
