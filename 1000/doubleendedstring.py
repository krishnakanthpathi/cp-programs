def main():
    a = input()
    b = input()
    res = len(a) + len(b)
    for length in range(len(a), 0, -1):
        for i in range(len(a) - length + 1):
            if a[i:i+length] in b :
                a_ops = i + (len(a) - length - i)
                b_ops = b.index(a[i:i+length]) + (len(b) - length - b.index(a[i:i+length]))
                res = min(res, a_ops + b_ops)
    print(res)



t = int(input())
for _ in range(t):
    main()