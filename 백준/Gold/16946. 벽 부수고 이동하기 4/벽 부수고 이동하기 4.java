import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static int n, m;
    static int[][] arr;
    static int[][] group;
    static Map<Integer, Integer> map = new HashMap<>();
    static Queue<int[]> queue = new LinkedList<>();

    static final int CAN_GO = 0;
    static final int CANNOT_GO = 1;
    static final int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        n = temp[0];
        m = temp[1];

        arr = new int[n][m];
        group = new int[n][m];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().chars().map(c -> c - '0').toArray();
        }

        setGroup();
        setAnswer();
        print(arr);
    }

    private static void setGroup() {
        int groupNum = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == CAN_GO && group[i][j] == 0) {
                    groupNum++;
                    grouping(i, j, groupNum);
                }
            }
        }
    }

    private static void grouping(int y, int x, int groupNum) {
        int count = 0;
        queue.add(new int[]{y, x});
        group[y][x] = groupNum;

        while (!queue.isEmpty()) {
            int[] temp = queue.remove();

            int curY = temp[0];
            int curX = temp[1];
            count += 1;

            for (int i = 0; i < 4; i++) {
                int nextY = curY + d[i][0];
                int nextX = curX + d[i][1];

                if (nextY < 0 || nextY >= n || nextX < 0 || nextX >= m) {
                    continue;
                }

                if (arr[nextY][nextX] == CAN_GO && group[nextY][nextX] == 0) {
                    queue.add(new int[]{nextY, nextX});
                    group[nextY][nextX] = groupNum;
                }
            }
        }
        map.put(groupNum, count);
    }

    private static void setAnswer() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == CANNOT_GO) {
                    Set<Integer> surroundGroupNum = new HashSet<>();

                    for (int k = 0; k < 4; k++) {
                        int nextY = i + d[k][0];
                        int nextX = j + d[k][1];

                        if (nextY < 0 || nextY >= n || nextX < 0 || nextX >= m) {
                            continue;
                        }

                        surroundGroupNum.add(group[nextY][nextX]);
                    }

                    arr[i][j] = surroundGroupNum.stream()
                            .filter(groupNum -> groupNum != 0)
                            .mapToInt(groupNum -> map.get(groupNum))
                            .sum() + 1;
                }
            }
        }
    }

    private static void print(int[][] arr) {
        for (int[] row : arr) {
            for (int col : row) {
                System.out.print(col % 10);
            }
            System.out.println();
        }
    }
}