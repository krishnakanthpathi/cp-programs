
def main():
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    median = (n + 1) // 2
    right = 0
    total = 0
    for i in range(n*k - 1, -1, -1):
        if total == k:
            break
        # print(right , n - median , res)
        if right >= n - median:
            res += arr[i]
            total += 1
            right -= n - median
        else:
            right += 1
        
    print(res)
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()