def main() :
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for i in range(n) :
        if arr[i] not in freq :
            freq[arr[i]] = [[] , [0 , 0]]
        freq[arr[i]][0].append(i + 1)
        freq[arr[i]][1][1] += 1
    for v in freq.values() :
        if len(v[0]) < 2:
            print(-1)
            return
    ans = []
    
    print(' '.join(map(str, ans)))
    
if __name__ == "__main__" :
    for _ in range(int(input())) :
        main()
        