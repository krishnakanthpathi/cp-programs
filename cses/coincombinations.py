from functools import cache
n , x = map(int , input().split())

c = list(map(int , input().split()))

MOD = int(10**9 + 7)

# @cache
# def dfs(cur) :
#     if cur == 0 :
#         return 1

#     if cur < 0 :
#         return 0
        
#     res = 0

#     for i in c:
#         res = (res + dfs(cur - i)) % MOD
#     return res

# print(dfs(x) % MOD)


dp = [0] * (x + 1)
dp[0] = 1

for i in range(1 , x + 1) :
    for j in c :
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % MOD

print(dp[x])
