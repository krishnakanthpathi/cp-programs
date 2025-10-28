import math

def main() :
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    left = 0
    res = 0
    right = n - 1
    while left <= right :
        if arr[right] > k :
            res += 1
            right -= 1
            continue
        nos = k // arr[right] + 1
        if nos <= right - left + 1 :
            res += 1
        left += nos - 1
        right -= 1
    print(res)
        

    
    
if __name__ == "__main__" :
    main()