import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Main {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    static final char COIN = 'o';
    static final char WALL = '#';

    static int n, m;
    static boolean[][][][] isVisited;
    static char[][] arr;
    static Queue<int[]> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        n = temp[0];
        m = temp[1];

        arr = new char[n][m];
        isVisited = new boolean[n][m][n][m];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        List<int[]> coins = findCoins();

        int[] coins1 = coins.get(0);
        int[] coins2 = coins.get(1);

        queue.add(new int[]{coins1[0], coins1[1], coins2[0], coins2[1], 0});
        isVisited[coins1[0]][coins1[1]][coins2[0]][coins2[1]] = true;

        int result=bfs();
        System.out.println(result);
    }

    private static int bfs() {
        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int y1 = temp[0];
            int x1 = temp[1];
            int y2 = temp[2];
            int x2 = temp[3];
            int current = temp[4];

            if (current >= 10) {
                return -1;
            }

            for (int i = 0; i < 4; i++) {
                int nextY1 = y1 + dy[i];
                int nextX1 = x1 + dx[i];
                int nextY2 = y2 + dy[i];
                int nextX2 = x2 + dx[i];
                int next = current + 1;

                if (isRange(nextY1, nextX1) && isRange(nextY2, nextX2)) {
                    if (isVisited[nextY1][nextX1][nextY2][nextX2]) {
                        continue;
                    }

                    if (arr[nextY1][nextX1] == WALL && arr[nextY2][nextX2] == WALL) {
                        continue;
                    }

                    else if (arr[nextY1][nextX1] == WALL && arr[nextY2][nextX2] != WALL) {
                        queue.add(new int[]{y1, x1, nextY2, nextX2, next});
                        isVisited[y1][x1][nextY2][nextX2] = true;
                    }
                    else if (arr[nextY2][nextX2] == WALL && arr[nextY1][nextX1] != WALL) {
                        queue.add(new int[]{nextY1, nextX1, y2, x2, next});
                        isVisited[nextY1][nextX1][y2][x2] = true;
                    }

                    else{
                        queue.add(new int[]{nextY1, nextX1, nextY2, nextX2, next});
                        isVisited[nextY1][nextX1][nextY2][nextX2] = true;
                    }
                }
                else if (!isRange(nextY1, nextX1) && isRange(nextY2, nextX2)) {
                    return next;
                }
                else if (isRange(nextY1, nextX1) && !isRange(nextY2, nextX2)) {
                    return next;
                }
            }
        }
        return -1;
    }
    private static List<int[]> findCoins(){
        List<int[]> coins = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == COIN) {
                    coins.add(new int[]{i, j, 0});
                }

                if (coins.size() == 2) {
                    return coins;
                }
            }
        }
        throw new IllegalArgumentException("코인이 2개 이상 없습니다.");
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < n && x >= 0 && x < m;
    }
}