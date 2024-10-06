import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    static final int MAX = 8;
    static final char WALL = '#';
    static final char EMPTY = '.';

    static Queue<int[]> queue = new LinkedList<>();

    static final int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}, {0, 0}};

    static char[][] arr;
    static boolean[][] isVisited;

    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new char[MAX][MAX];
        for (int i = 0; i < MAX; i++) {
            arr[i] = br.readLine().toCharArray();
        }
        bfs(MAX - 1, 0);
    }

    private static void bfs(int y, int x) {
        queue.add(new int[]{y, x, 1});
        while (!queue.isEmpty()) {
            isVisited = new boolean[MAX][MAX];
            boolean result = movePerson();

            if (result) {
                answer = 1;
                break;
            }
            moveWall();
        }

        System.out.println(answer);
    }

    private static boolean movePerson() {
        int size = queue.size();

        for (int i = 0; i < size; i++) {
            int[] temp = queue.remove();

            int currentY = temp[0];
            int currentX = temp[1];
            int count = temp[2];

            char current = arr[currentY][currentX];

            if (current == WALL) {
                continue;
            }

            if (count >= 8) {
                return true;
            }

            for (int j = 0; j < d.length; j++) {
                int nextY = currentY + d[j][0];
                int nextX = currentX + d[j][1];

                if (nextY == 0 && nextX == MAX - 1) {
                    return true;
                }

                if (canGo(nextY, nextX)) {
                    queue.add(new int[]{nextY, nextX, count + 1});
                    isVisited[nextY][nextX] = true;
                }
            }
        }
        return false;
    }

    private static void moveWall() {
        for (int i = MAX - 1; i >= 0; i--) {
            for (int j = 0; j < MAX; j++) {
                if (arr[i][j] == WALL) {
                    arr[i][j] = EMPTY;
                    if (canMoveWall(i + 1)) {
                        arr[i + 1][j] = WALL;
                    }
                }
            }
        }
    }

    private static boolean canGo(int y, int x) {
        return isRange(y, x) && !isVisited[y][x] && arr[y][x] == EMPTY;
    }

    private static boolean canMoveWall(int y) {
        return y >= 0 && y < MAX;
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < MAX && x >= 0 && x < MAX;
    }

}