
def main() :
    n , x = map(int, input().split())
    arr = list(map(int, input().split()))
    l , r = abs(arr[0] - x) , abs(arr[0] + x)
    res = 0
    for i in range(1, n) :
        cur = arr[i]
        cur_l , cur_r = abs(cur - x) , abs(cur + x)
        # print(l , r , cur_l , cur_r)
        if l <= cur_l <= r or l <= cur_r <= r or cur_l <= l <= cur_r or cur_l <= r <= cur_r :
            l = max(l, cur_l)
            r = min(r, cur_r)
        else :
            res += 1
            l , r = cur_l , cur_r
    print(res )
    
if __name__ == "__main__" :
    for _ in range(int(input())) :
        main()