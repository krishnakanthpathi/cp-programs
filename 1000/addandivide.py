import math

def main():
    a , b  = map(int , input().split())
    ops = float("inf")
    for i in range(33):
        if b + i == 1:
            ops = min(ops, a + b)
            if a < b:
                ops = 1
            continue
        
        # Calculate divisions using log + adjustment
        base = b + i
        val = int(math.log(a, base))
        if base ** (val + 1) <= a:
            val += 1
        divisions = val + 1

        ops = min(ops, i + divisions)

    print(ops if ops != float("inf") else 0)
    

t = int(input())
for _ in range(t) :
    main()