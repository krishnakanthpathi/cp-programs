# from functools import cache

n , k = map(int ,input().split())
heights = list(map(int ,input().split()))

# @cache
# def dfs(i) :
#     if i == n - 1:
#         return 0
#     if i >= n:
#         return float('inf')
    
#     jumps = float('inf')
#     for j in range(1, k + 1):
#         if i + j < n:
#             jumps = min(jumps, dfs(i + j) + abs(heights[i] - heights[i + j]))
#     return jumps

jumps = [float("inf")] * (n + 1)
jumps[0] = 0

for i in range(1, n):
    for j in range(1, k + 1):
        if i - j >= 0:
            jumps[i] = min(jumps[i], jumps[i - j] + abs(heights[i] - heights[i - j]))
print(jumps[n - 1])
