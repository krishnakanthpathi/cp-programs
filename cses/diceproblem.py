# from functools import cache
# import sys


# MOD = 10**9 + 7

# n = int(input())

# dp = [0] * (n + 1)
# dp[0] = 1

# for i in range(1, n + 1):
#     for j in range(i - 6 , i):
#         if j >= 0:
#             dp[i] = (dp[i] + dp[j]) % MOD

# print(dp[n])
# sys.exit()

# @cache
# def dfs(cur):
#     if cur < 0 :
#         return 0
#     if cur == 0 :
#         return 1
#     res = 0
#     for i in range(1, 7):
#         res = (res + dfs(cur - i)) % MOD
#     return res

# print(dfs(n))


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()

MOD = int(10**9 + 7)
n = int(input())
# 6
# 0 1 2 3 4 5 
# 0 1 2 3 
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2 , n + 1):
    for j in range(1 , 7):
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % MOD
    # print(dp)
print(dp[n])






