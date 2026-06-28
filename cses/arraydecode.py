



from functools import cache

n , m = map(int ,input().split())
arr = list(map(int , input().split()))

MOD = int(1e9 + 7)

def solve(n , k , arr) :
    @cache
    def dfs(idx , prev) :

        if idx == n :
            return 1
        
        if arr[idx] != 0 :
            if abs(arr[idx] - prev) > 1 :
                return 0
            return dfs(idx + 1 , arr[idx])

        res = 0
        for i in range(1 , m + 1) :
            if abs(i - prev) <= 1 or prev == float("inf"):
                ans = dfs(idx + 1 , i)
                res =  (res +  ans )% MOD 
        return res 


    return dfs(0 , float("inf"))
        
print(solve(n , m , arr))