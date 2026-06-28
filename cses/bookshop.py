

from functools import cache
def main(n , x , costs , pages) :
    
    dp = [0] * (x + 1)
    
    for i in range(n) :
        cost = costs[i]
        page = pages[i]
        for j in range(x, cost - 1, -1) :
            dp[j] = max(dp[j], dp[j - cost] + page)

    return dp[x]


    @cache
    def dfs(idx , cur) :

        if idx == n :
            return 0

        if cur + costs[idx] > x :
            return dfs(idx + 1 , cur)
        pick =  pages[idx] + dfs(idx + 1 , cur + costs[idx])
        nopick = dfs(idx + 1 , cur)
        return max(pick , nopick)
    return dfs(0 , 0)


n, x = map(int , input().split())
costs = list(map(int , input().split()))
pages = list(map(int , input().split()))
print(main(n , x , costs , pages))