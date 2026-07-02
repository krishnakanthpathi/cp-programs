



from functools import cache

n , m = map(int ,input().split())
arr = list(map(int , input().split()))

MOD = int(1e9 + 7)


dp = [
  [ 0  for j in range(m + 1) ] for i in range(n + 1)
]

# we will find the number of arrays of prefix
# such that it having a k as the element previous


for i in range(n):

    if arr[i] == 0 :
        for j in range(1 , m + 1) :
            
            if i == 0 :
                dp[0][j] = 1 
                continue

            dp[i][j] = sum([
                dp[i - 1][j] if i - 1 >= 0 else (
                    1 if arr[i - 1] != 0 and j == arr[i - 1]  else 0
                ) , 
                dp[i - 1][j - 1] if i - 1 >= 0  and j - 1 >= 0  else  0, 
                dp[i - 1][j + 1] if i - 1 >= 0 and j + 1 <= m  else 0 
                ]) % MOD 
        
    else:
        dp[i][arr[i]] = sum([
            dp[i - 1][arr[i]] if i - 1 >= 0 else 1, 
            dp[i - 1][arr[i] - 1] if i - 1 >= 0 and arr[i] - 1 >= 0 else 0 , 
            dp[i - 1][arr[i] + 1] if i - 1 >= 0 and arr[i] + 1 <= m  else 0 
            ]) % MOD
    # print(dp[i] )

if arr[-1] == 0 :
    print(sum(dp[n-1])%MOD)
else:
    print(dp[n-1][arr[-1]]%MOD)














# def solve(n , k , arr) :
#     @cache
#     def dfs(idx , prev) :

#         if idx == n :
#             return 1
        
#         if arr[idx] != 0 :
#             if abs(arr[idx] - prev) > 1 :
#                 return 0
#             return dfs(idx + 1 , arr[idx])

#         res = 0
#         for i in range(1 , m + 1) :
#             if abs(i - prev) <= 1 or prev == float("inf"):
#                 ans = dfs(idx + 1 , i)
#                 res =  (res +  ans )% MOD 
#         return res 


#     return dfs(0 , float("inf"))
        
# print(solve(n , m , arr))