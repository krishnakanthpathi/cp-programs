from functools import cache
import sys
# sys.setrecursionlimit(2000000)
n , x = map(int, input().split())
c = list(map(int, input().split()))

# @cache
# def dfs(cur) :
#     if cur == 0 :
#         return 0
#     if cur < 0 :
#         return float("inf")
#     res = float("inf")
#     for ci in c :
#         res = min(res , dfs(cur - ci) + 1)
#     return res 
    
# ans = dfs(x)


dp = [float("inf")]*(x + 1)
dp[0] = 0
for i in range(1 , x + 1) :
    for ci in c :
        if i - ci >= 0 :
            dp[i] = min(dp[i] , dp[i - ci] + 1)

    


if dp[x] == float("inf") :
    print(-1)
else :
    print(dp[x])