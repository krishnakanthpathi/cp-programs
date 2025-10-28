

def find(l , r , k):
    n = r - l - ( k - 1 )
    if n <= 0 :
        return 0
    total = n * (n + 1) // 2
    return total
def main():
    n, k , x = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    l = 0
    for r in range(n):
        if a[r] > x :
            res += find(l , r , k) 
            # print(find(l , r ,k) , r)
            l = r + 1
    
    res += find(l , r + 1 , k )
    print(res)
        
        
    
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()