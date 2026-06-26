
import java.util.*;

public class gridpaths {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int grid[][] = new int[n][n];

        for (int i = 0; i < n; i++) {
            String row = sc.next();
            for (int j = 0; j < n; j++) {
                if (row.charAt(j) == '*') {
                    grid[i][j] = 1;
                } else {
                    grid[i][j] = 0;
                }
            }
        }
        long MOD = 1_000_000_000 + 7;
        long dp[][] = new long[n + 1][n + 1];
        dp[n - 1][n - 1] = 1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i == n - 1 && j == n - 1) {
                    if (grid[i][j] == 1) {
                        dp[i][j] = 0;
                    }
                    continue;
                }

                if (grid[i][j] == 1) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = (dp[i + 1][j] + dp[i][j + 1]) % MOD;
                }

            }
        }
        System.out.println(dp[0][0]);

        sc.close();

    }

}
