def main():
    n = int(input())
    binary = str(bin(n)[2:])
    if binary.count('1') == 1:
        print("NO")
        return
    print("YES")
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()