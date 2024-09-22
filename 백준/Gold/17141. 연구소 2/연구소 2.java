import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static final int EMPTY = 0;
    static final int WALL = -1;
    static final int CAN_VIRUS = 2;
    static final int VIRUS = 3;

    static int N, M;
    static int[][] arr;
    static Set<Integer> results = new HashSet<>();

    static Queue<int[]> queue = new LinkedList<>();
    static List<int[]> canVirus = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        N = temp[0];
        M = temp[1];

        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == CAN_VIRUS) {
                    canVirus.add(new int[]{i, j});
                }
            }
        }

        setVirus(0, 0, new LinkedList<>());

        Integer result = results.stream().filter(x -> x != -1).min(Integer::compare).orElse(-1);
        System.out.println(result);

    }

    private static void setVirus(int start, int count, List<int[]> selectedPositions) {
        if (count == M) {
            execute(selectedPositions);
            return;
        }

        for (int i = start; i < canVirus.size(); i++) {
            selectedPositions.add(canVirus.get(i));
            setVirus(i+1, count + 1, selectedPositions);
            selectedPositions.remove(selectedPositions.size() - 1);
        }
    }

    private static void execute(List<int[]> selectedPositions) {
        int[][] arr = copy();
        boolean[][] isVisited = new boolean[N][N];

        for (int[] pos : selectedPositions) {
            int x = pos[0];
            int y = pos[1];

            isVisited[x][y] = true;
            arr[x][y] = -1;
            queue.add(new int[]{x, y, 0});
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == VIRUS) {
                    isVisited[i][j] = true;
                    arr[i][j] = -1;
                    queue.add(new int[]{i, j, 0});
                }
                if (arr[i][j] == CAN_VIRUS) {
                    arr[i][j] = EMPTY;
                }

                if (arr[i][j] == 1) {
                    arr[i][j] = WALL;
                }
            }
        }

        spreadVirus(arr, isVisited);
    }

    // empty, virus , wall 종류만 있다.
    private static void spreadVirus(int[][] arr, boolean[][] isVisited) {
        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int currentX = temp[0];
            int currentY = temp[1];
            int currentCount = temp[2];

            for (int i = 0; i < 4; i++) {
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];

                if (canGo(nextX, nextY, isVisited, arr)) {
                    isVisited[nextX][nextY] = true;
                    int nextCount = currentCount + 1;
                    arr[nextX][nextY] = nextCount;
                    queue.add(new int[]{nextX, nextY, nextCount});
                }
            }
        }

        int max = findMax(arr);

        results.add(max);
    }

    private static boolean isRange(int x, int y) {
        return x >= 0 && y >= 0 && x < N && y < N;
    }

    private static boolean canGo(int x, int y, boolean[][] isVisited, int[][] arr) {
        return isRange(x, y) && arr[x][y] == EMPTY && !isVisited[x][y];
    }

    private static int findMax(int[][] arr) {
        int result = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int temp = arr[i][j];

                if (temp == EMPTY) {
                    return -1;
                }

                if (temp > result) {
                    result = temp;
                }
            }
        }

        return result;
    }

    private static int[][] copy() {
        int[][] copy = new int[N][N];

        for (int i = 0; i < N; i++) {
            copy[i] = Arrays.copyOf(arr[i], N);
        }

        return copy;
    }
}