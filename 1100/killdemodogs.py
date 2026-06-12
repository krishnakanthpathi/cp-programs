# Constant for modulo operation
MOD = 1000000007

t = int(input())

for _ in range(t):
    n = int(input())
    ans = ((((n * (n + 1)) % MOD) * (4 * n - 1)) % MOD * 337) % MOD
    print(ans)
