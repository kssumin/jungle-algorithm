import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static int n;
    static int[][] arr;

    static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        setTeam(0, 0, new ArrayList<>());

        System.out.println(result);
    }


    private static void setTeam(int start, int count, List<Integer> selectMember) {
        if (count == n / 2) {
            execute(selectMember);
            return;
        }

        for (int i = start; i < n; i++) {
            selectMember.add(i);
            setTeam(i + 1, count + 1, selectMember);
            selectMember.remove(selectMember.size() - 1);
        }
    }

    private static int calculate(List<Integer> selectedMembers) {
        int synergy = 0;

        for (int i = 0; i < selectedMembers.size() - 1; i++) {
            for (int j = i + 1; j < selectedMembers.size(); j++) {
                int member1 = selectedMembers.get(i);
                int member2 = selectedMembers.get(j);
                synergy += arr[member1][member2];
                synergy += arr[member2][member1];
            }
        }
        return synergy;
    }

    private static void execute(List<Integer> members) {
        List<Integer> unselectedMembers = getUnselectedMembers(members);

        int teamASynergy = calculate(unselectedMembers);
        int teamBSynergy = calculate(members);

        int diff = Math.abs(teamASynergy - teamBSynergy);

        if (diff == 0) {
            result = diff;
            return;
        }

        if (diff < result) {
            result = diff;
        }
    }

    private static List<Integer> getUnselectedMembers(List<Integer> selectedMembers) {
        List<Integer> unselectedMembers = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!selectedMembers.contains(i)) {
                unselectedMembers.add(i);
            }
        }
        return unselectedMembers;
    }
}
