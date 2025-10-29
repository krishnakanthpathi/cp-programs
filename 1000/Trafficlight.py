from bisect import bisect_left

def main():
    n , c = input().split()
    n = int(n)
    string = input().strip()
    res = []
    ans = float('-inf')
    for i in range(n):
        if string[i] == 'g':
            res.append(i)
    
    for i in range(n):
        if string[i] == c :
            idx = bisect_left(res, i)
            if idx == len(res):
                idx = 0
            ans = max(ans, (res[idx] - i) % n)
    
    print(ans)
    
    
if __name__ == "__main__":
    for _ in range(int(input())):
        main()