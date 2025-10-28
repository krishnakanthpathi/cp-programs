
def main():
    n , k = map(int, input().split())
    a = list(map(int, input().split()))
    res = 1
    for i in range(n):
        res = (res * a[i]) % k
    print(res)


if __name__ == "__main__":
    for _ in range(int(input())):
        main()