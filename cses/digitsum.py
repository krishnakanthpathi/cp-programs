

n = int(input())

dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1 , n + 1):
    for digit in str(i) :
        j = int(digit)
        if i - j >= 0:
            dp[i] = min(dp[i] , 1 + dp[i - j])


print(dp[n])