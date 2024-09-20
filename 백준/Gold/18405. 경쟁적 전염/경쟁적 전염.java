import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Main {
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    static int N, K, S, X, Y;
    static int[][] arr;

    static List<List<int[]>> list = new LinkedList<>();
    static Queue<int[]> queue = new LinkedList<>();
    static boolean[][] isVisited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        N = temp[0];
        K = temp[1];

        arr = new int[N][N];
        isVisited = new boolean[N][N];

        for (int i = 0; i < K + 1; i++) {
            list.add(new LinkedList<>());
        }

        for (int i = 0; i < N; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        S = temp[0];
        X = temp[1];
        Y = temp[2];

        // 1 ~ K번 바이러스까지의 위치를 저장
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int target = arr[i][j];

                if (target == 0) {
                    continue;
                }
                list.get(target).add(new int[]{i, j});
            }
        }

        // 초기값 넣기
        for (List<int[]> ints : list) {
            for (int[] anInt : ints) {
                int y = anInt[0];
                int x = anInt[1];

                queue.add(new int[]{y, x, 0});
                isVisited[y][x] = true;
            }
        }

        bfs();
        System.out.println(arr[X - 1][Y - 1]);
    }

    private static void bfs() {
        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            if (temp[2] == S) {
                break;
            }

            int currentY = temp[0];
            int currentX = temp[1];
            int time = temp[2];

            int currentVirus = arr[currentY][currentX];

            for (int i = 0; i < 4; i++) {
                int nextY = currentY + dy[i];
                int nextX = currentX + dx[i];

                if (canGo(nextY, nextX)) {
                    arr[nextY][nextX] = currentVirus;
                    queue.add(new int[]{nextY, nextX, time + 1});
                    isVisited[nextY][nextX] = true;
                }
            }
        }
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < N && x >= 0 && x < N;
    }

    private static boolean canGo(int y, int x) {
        return isRange(y, x) && !isVisited[y][x];
    }
}