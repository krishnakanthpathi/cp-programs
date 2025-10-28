from collections import defaultdict

def main():
    n  = int(input())
    string = input().strip()
    left = defaultdict(int)
    right = defaultdict(int)
    for i in range(n):
        left[string[i]] += 1
    res = 0
    for i in range(n - 1, -1, -1):
        left[string[i]] -= 1
        right[string[i]] += 1
        if left[string[i]] == 0:
            del left[string[i]]
        res = max(res , len(left) + len(right))
    print(res)
    
if __name__ == "__main__":
    for _ in range(int(input())):
        main()