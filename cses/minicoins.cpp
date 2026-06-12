#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, x;
    if (!(cin >> n >> x)) return 0;
    
    vector<int> c(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }
    
    vector<int> dp(x + 1, 1e9);
    dp[0] = 0;
    
    for (int i = 1; i <= x; i++) {
        for (int ci : c) {
            if (i - ci >= 0) {
                dp[i] = min(dp[i], dp[i - ci] + 1);
            }
        }
    }
    
    if (dp[x] == 1e9) {
        cout << -1 << "\n";
    } else {
        cout << dp[x] << "\n";
    }
    
    return 0;
}