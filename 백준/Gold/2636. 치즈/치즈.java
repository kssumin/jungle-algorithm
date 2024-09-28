import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static final int AIR = 0;
    static final int CHEESE = 1;

    static int n, m;
    static int[][] arr;
    static boolean[][] isVisited;

    static Queue<int[]> airQueue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = temp[0];
        m = temp[1];

        arr = new int[n][m];
        isVisited = new boolean[n][m];

        for (int j = 0; j < n; j++) {
            arr[j] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        int[] results = execute();

        System.out.println(results[0]);
        System.out.println(results[1]);
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < n && x >= 0 && x < m;
    }

    private static boolean canGo(int y, int x) {
        return isRange(y, x) && !isVisited[y][x];
    }
    

    private static int[] execute() {
        int retryCount = 0;
        int cheese = 0;

        // 치즈가 모두 녹을 때까지 반복한다.
        while (!isAllMelt()) {
            cheese = getCheese();
            retryCount += 1;

            for (boolean[] booleans : isVisited) {
                Arrays.fill(booleans, false);
            }

            findAir();
            meltCheese();
        }
        return new int[]{retryCount, cheese};
    }

    private static void findAir() {
        airQueue.add(new int[]{0, 0});
        isVisited[0][0] = true;
    }

    private static void meltCheese() {
        while (!airQueue.isEmpty()) {
            int[] temp = airQueue.remove();

            int y = temp[0];
            int x = temp[1];

            for (int i = 0; i < 4; i++) {
                int nextY = y + dy[i];
                int nextX = x + dx[i];

                if (canGo(nextY, nextX)) {
                    if (arr[nextY][nextX] == CHEESE) {
                        arr[nextY][nextX] = AIR;
                        isVisited[nextY][nextX] = true;
                    }
                    else{
                        airQueue.add(new int[]{nextY, nextX});
                        isVisited[nextY][nextX] = true;
                    }
                }
            }
        }
    }


    private static int getCheese() {
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == CHEESE) {
                    count += 1;
                }
            }
        }
        return count;
    }

    private static boolean isAllMelt() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == CHEESE) {
                    return false;
                }
            }
        }
        return true;
    }
}
