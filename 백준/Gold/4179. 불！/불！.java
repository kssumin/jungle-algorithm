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
    static final char PERSON = 'J';
    static final char FIRE = 'F';

    static int n, m;
    static char[][] arr;
    static boolean[][] isVisitedPerson;

    static Queue<int[]> fire;
    static Queue<int[]> person;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = temp[0];
        m = temp[1];

        arr = new char[n][m];
        isVisitedPerson = new boolean[n][m];
        fire = new LinkedList<>();
        person = new LinkedList<>();


        for (int j = 0; j < n; j++) {
            arr[j] = br.readLine().toCharArray();
        }

        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                if (arr[j][k] == FIRE) {
                    fire.add(new int[]{j, k});
                }

                if (arr[j][k] == PERSON) {
                    person.add(new int[]{j, k, 0});
                    isVisitedPerson[j][k] = true;
                }
            }
        }
        int result = bfs();

        sb.append(result == -1 ? "IMPOSSIBLE" : result);
        sb.append("\n");

        System.out.println(sb);
    }

    private static boolean isExit(int y, int x) {
        return y == n - 1 || y == 0 || x == m - 1 || x == 0;
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < n && x >= 0 && x < m;
    }

    private static int bfs() {
        // 사람이 더 이상 움직일 곳이 없다는 뜻
        while (!person.isEmpty()) {
            spreadFire();
            int mid = movePerson();

            if (mid != -1) {
                return mid;
            }
        }
        return -1;
    }

    private static void spreadFire() {
        int size = fire.size();

        // 처음에 불 사이즈 만큼만 확장한다.
        for (int j = 0; j < size; j++) {
            int[] temp = fire.remove();

            int y = temp[0];
            int x = temp[1];

            for (int i = 0; i < 4; i++) {
                int nextY = y + dy[i];
                int nextX = x + dx[i];

                if (isRange(nextY, nextX)) {
                    // 사람, 빈 경우에만 불을 붙일 수 있다.
                    if (arr[nextY][nextX] == PERSON || arr[nextY][nextX] == EMPTY) {
                        arr[nextY][nextX] = FIRE;
                        fire.add(new int[]{nextY, nextX});
                    }
                }
            }
        }
    }

    private static int movePerson() {
        int personSize = person.size();

        for (int j = 0; j < personSize; j++) {
            int[] temp = person.remove();

            int y = temp[0];
            int x = temp[1];
            int count = temp[2];

            if (isExit(y, x)) {
                return count + 1;
            }

            for (int i = 0; i < 4; i++) {
                int nextY = y + dy[i];
                int nextX = x + dx[i];

                if (isRange(nextY, nextX) && !isVisitedPerson[nextY][nextX]) {
                    if (arr[nextY][nextX] == EMPTY) {
                        arr[nextY][nextX] = PERSON;
                        person.add(new int[]{nextY, nextX, count + 1});
                        isVisitedPerson[nextY][nextX] = true;

                        if (arr[y][x] == PERSON) {
                            arr[y][x] = EMPTY;
                        }
                    }
                }
            }
        }
        return -1;
    }
}
