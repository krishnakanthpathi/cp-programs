from functools import cache
class Solution:
    def frogJump(self, heights):
        n = len(heights)

        @cache
        def dfs(i) :
            if i == n - 1:
                return 0
            if i >= n:
                return float('inf')
            
            onejump = dfs(i + 1) + (abs(heights[i] - heights[i + 1]) if i + 1 < n else float('inf'))
            twojump = dfs(i + 2) + (abs(heights[i] - heights[i + 2]) if i + 2 < n else float('inf'))

            return min(onejump, twojump)

        # Memoization to avoid recomputation
        return dfs(0)
    
    def frogJumpTabulation(self, heights):
        n = len(heights)
        dp = [0] * n
        
        for i in range(1, n):
            onejump = dp[i - 1] + abs(heights[i] - heights[i - 1])
            twojump = dp[i - 2] + abs(heights[i] - heights[i - 2]) if i > 1 else float('inf')
            dp[i] = min(onejump, twojump)
        return dp[-1]
        
        

                
        
    
# Example usage:
n = int(input())  # Input: number of stones
heights = list(map(int ,input().split()))  # Input: heights of the stones
solution = Solution()
print(solution.frogJumpTabulation(heights))  # Output: 30 (minimum cost to reach the end)