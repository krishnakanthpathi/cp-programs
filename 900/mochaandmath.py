def main() :
    n = int(input())
    arr = [int(val) for val in input().split()]
    res = arr[0]
    for val in arr :
        res = res & val
    print(res)
    
if __name__ == "__main__" :
    t = int(input())
    for _ in range(t)  :
        main()