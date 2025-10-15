def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            print("YES")
            print(i, i+1, i+2)
            return
    
    
    print("NO")
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()