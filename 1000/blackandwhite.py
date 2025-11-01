
def main():
    n , k = map(int, input().split())
    string = input().strip()
    black , white = 0 , 0
    l = 0
    res = k
    for r in range(n):
        if string[r] == 'B':
            black += 1
        else:
            white += 1
        
        if r - l + 1 > k:
            if string[l] == 'B':
                black -= 1
            else:
                white -= 1
            l += 1
        
        if r - l + 1 == k:
            res = min(res , white)
    print(res)
if __name__ == "__main__":
    for _ in range(int(input())):
        main()