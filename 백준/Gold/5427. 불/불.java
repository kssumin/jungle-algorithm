import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static final char EMPTY = '.';
    static final char PERSON = '@';
    static final char FIRE = '*';

    static int n, m;
    static char[][] arr;
    static boolean[][] isVisitedFire;
    static boolean[][] isVisitedPerson;
    static Queue<int[]> queue;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            m = temp[0];
            n = temp[1];

            arr = new char[n][m];
            isVisitedFire = new boolean[n][m];
            isVisitedPerson = new boolean[n][m];
            queue = new LinkedList<>();


            for (int j = 0; j < n; j++) {
                arr[j] = br.readLine().toCharArray();
            }


            int[] start = new int[0];

            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (arr[j][k] == FIRE) {
                        queue.add(new int[]{j, k, FIRE, 0});
                        isVisitedFire[j][k] = true;
                    }

                    if (arr[j][k] == PERSON) {
                        start = new int[]{j, k, PERSON, 0};
                        isVisitedPerson[j][k] = true;
                    }
                }
            }
            queue.add(start);

            int result = bfs();


            sb.append(result == -1 ? "IMPOSSIBLE" : result);
            sb.append("\n");
        }

        System.out.println(sb);
    }

    private static boolean isExit(int y, int x) {
        return y == n - 1 || y == 0 || x == m - 1 || x == 0;
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < n && x >= 0 && x < m;
    }

    private static int bfs() {
        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int y = temp[0];
            int x = temp[1];
            char type = (char) temp[2];
            int count = temp[3];

            if (isExit(y, x) && type == PERSON) {
                return count + 1;
            }

            for (int i = 0; i < 4; i++) {
                int nextY = y + dy[i];
                int nextX = x + dx[i];

                if (isRange(nextY, nextX)) {
//                    System.out.println("y: " + y + ", x: " + x + ", nextY: " + nextY + ", nextX: " + nextX);
//                    System.out.println("type: " + type + ", count: " + count);

                    if (type == PERSON && !isVisitedPerson[nextY][nextX]) {
                        if (arr[nextY][nextX] == EMPTY) {
                            arr[nextY][nextX] = PERSON;
                            queue.add(new int[]{nextY, nextX, PERSON, count + 1});
                            isVisitedPerson[nextY][nextX] = true;

                            if (arr[y][x] == PERSON) {
                                arr[y][x] = EMPTY;
                            }
                        }
                    }

                    if (type == FIRE && !isVisitedFire[nextY][nextX]) {
                        // 사람, 빈 경우에만 불을 붙일 수 있다.
                        if (arr[nextY][nextX] == PERSON || arr[nextY][nextX] == EMPTY) {
                            arr[nextY][nextX] = FIRE;
                            queue.add(new int[]{nextY, nextX, FIRE, count + 1});
                            isVisitedFire[nextY][nextX] = true;
                        }
                    }
                }
            }
        }
        return -1;
    }
}
