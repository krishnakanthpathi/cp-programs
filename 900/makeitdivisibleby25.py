
def main():
    n = int(input())
    res = float('inf')
    for pattern in ["00", "52", "05", "57"]:
        s = str(n)[::-1]
        idx = 0
        count = 0
        for i in range(len(s)):
            if  s[i] != pattern[idx]:
                count = count + 1
            else:
                idx += 1
            if idx == 2:
                res = min(res, count) 
                break    
    print(res)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()