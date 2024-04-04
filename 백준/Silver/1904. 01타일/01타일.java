import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 지금 관심있는게 N일 때 나올 수 있는 개수이다.
 * 그럼 우선 개수간의 관계를 파악해보자!
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 2];

        arr[1] = 1;
        arr[2] = 2;

        for (int i = 3; i < N + 1; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 15746;
        }

        br.close();
        System.out.println(arr[N]);
    }
}
