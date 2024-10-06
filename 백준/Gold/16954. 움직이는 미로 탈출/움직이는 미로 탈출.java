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
    static Queue<int[]> wallQueue = new LinkedList<>();

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
        findWall();
        bfs(MAX - 1, 0);
    }

    private static void bfs(int y, int x) {
        queue.add(new int[]{y, x});
        int tryCount = 0;
        while (!queue.isEmpty()) {
            tryCount++;
            isVisited = new boolean[MAX][MAX];
            boolean result = movePerson();

            if (result || tryCount >= 8) {
                answer = 1;
                break;
            }
            moveWall();
        }

        System.out.println(answer);
    }

    private static boolean movePerson() {
        int size = queue.size();
        Queue<int[]> nextQueue = new LinkedList<>();

        for (int i = 0; i < size; i++) {
            int[] temp = queue.remove();

            int currentY = temp[0];
            int currentX = temp[1];

            if (arr[currentY][currentX] == WALL) {
                continue;
            }

            if (currentY == 0 && currentX == MAX - 1) {
                return true;
            }

            for (int[] move : d) {
                int nextY = currentY + move[0];
                int nextX = currentX + move[1];

                if (canGo(nextY, nextX) && (nextY == 0 || arr[nextY - 1][nextX] != WALL)) {
                    nextQueue.add(new int[]{nextY, nextX});
                    isVisited[nextY][nextX] = true;
                }
            }
        }
        queue = nextQueue;
        return false;
    }

    private static void moveWall() {
        boolean[][] newWall = new boolean[MAX][MAX];
        int size = wallQueue.size();

        for (int i = 0; i < size; i++) {
            int[] temp = wallQueue.remove();

            int currentY = temp[0];
            int currentX = temp[1];
            arr[currentY][currentX] = EMPTY;

            int nextY = currentY + 1;

            if (canMoveWall(nextY)) {
                newWall[nextY][currentX] = true;
            }
        }

        for (int i = 0; i < MAX; i++) {
            for (int j = 0; j < MAX; j++) {
                if (newWall[i][j]) {
                    arr[i][j] = WALL;
                    wallQueue.add(new int[]{i, j});
                }
            }
        }
    }

    private static boolean canGo(int y, int x) {
        return isRange(y, x) && !isVisited[y][x] && arr[y][x] == EMPTY;
    }

    private static boolean canMoveWall(int y) {
        return y < MAX;
    }

    private static boolean isRange(int y, int x) {
        return y >= 0 && y < MAX && x >= 0 && x < MAX;
    }

    private static void findWall() {
        for (int i = 0; i < MAX; i++) {
            for (int j = 0; j < MAX; j++) {
                if (arr[i][j] == WALL) {
                    wallQueue.add(new int[]{i, j});
                }
            }
        }
    }
}