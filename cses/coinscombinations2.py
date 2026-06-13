from functools import cache
n , x = map(int , input().split())
coins = list(map(int , input().split()))
MOD = int(10**9 + 7)

@cache
def dfs(cur , idx):
    if cur == 0:
        return 1
    
    if cur < 0 or idx == n :
        return 0
    
    return dfs(cur - coins[idx] , idx ) + dfs(
        cur , idx + 1
    )



print(dfs(x , 0))



dp = [
    [0] * (n + 1) for i in range(x + 1)
]

