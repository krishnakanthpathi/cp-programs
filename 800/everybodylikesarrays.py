
def main() :
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(1 , n) :
        if a[i] % 2 == a[i - 1] % 2 :
            res += 1
    print(res)
if __name__ == "__main__" :
    t = int(input())
    for _ in range(t) :
        main()
