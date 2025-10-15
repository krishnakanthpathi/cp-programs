def main():
    n = int(input())
    cnt_2 = 0
    cnt_3 = 0
    while n and n % 2 == 0:
        cnt_2 += 1
        n //= 2
    while n and n % 3 == 0:
        cnt_3 += 1
        n //= 3
    if n > 1 or cnt_2 > cnt_3:
        print(-1)
        return
    print(cnt_3 + cnt_3 - cnt_2)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()