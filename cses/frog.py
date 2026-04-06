from functools import cache
n = int(input())
h = list(map(int, input().split()))


@cache
def dfs(i):
    if i >= n :
        return float('inf')
    if i == n - 1:
        return 0
    one = dfs(i + 1) + abs(h[i] - h[i + 1])
    two = dfs(i + 2) + abs(h[i] - h[i + 2]) if i + 2 <= n - 1 else float('inf')
    return min(one, two)
    
    
print(dfs(0))