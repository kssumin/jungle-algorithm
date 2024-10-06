import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Main {
    static final int MIN_V = 1;
    static final int MIN_C = 2;
    static final Set<Character> V = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

    static int totalCount, typeCount;
    static char[] arr;
    static boolean[] isVisited;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        totalCount = temp[0];
        typeCount = temp[1];

        arr = br.readLine().replaceAll(" ","").toCharArray();
        Arrays.sort(arr);

        isVisited = new boolean[typeCount];

        select(0, 0, 0, 0);
        System.out.println(sb);
    }

    private static void select(int start, int count, int v, int c) {
        if (count == totalCount) {
            if (valid(v, c)) {
                getValue();
            }
            return;
        }

        for (int i = start; i < typeCount; i++) {
            if (!isVisited[i]) {
                isVisited[i] = true;

                if (V.contains(arr[i])) {
                    select(i + 1, count + 1, v + 1, c);
                } else {
                    select(i + 1, count + 1, v, c + 1);
                }
                isVisited[i] = false;
            }
        }
    }

    private static boolean valid(int v, int c) {
        return v >= MIN_V && c >= MIN_C;
    }

    private static void getValue() {
        for (int i = 0; i < typeCount; i++) {
            if (isVisited[i]) {
                sb.append(arr[i]);
            }
        }
        sb.append("\n");
    }
}