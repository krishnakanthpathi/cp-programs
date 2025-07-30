t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    neg = sum(1 for i in a if i < 0)
    pos = sum(1 for i in a if i > 0)
    
    if neg % 2 == 0 and pos >= neg:
        print(0)
    elif neg % 2 == 0 and pos < neg:
        diff = neg - pos
        print(diff)
    elif neg % 2 == 1 and pos < neg:
        diff = neg - pos - 1
        print(diff//2 + 1 )