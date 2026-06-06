import math



def main():
    x , y , k = map(int, input().split())
    #  start  - 1 torch
    # k torches 
    
    # 1 + 1 + x + 1 + 2x .. 1 + (n - 1)*x >= n * k 
    
    # 5 --- k
    # 1 coalfor 1 stick
    # 2 sticks for 1 stick
    
    # k sticks 
    # 5 sticks + 5 coal( 5 sticks  )
    
    # 9 + (4 ops)

    # 1 , 2 , 3 , 4 , 5 = 10 4 ops

    # ops 1 + (p - 1) * n >= k
    #         (p - 1) * n >= k - 1
    #         n = math.ceil((k - 1) / (p - 1))

    sticks = k
    coals = k * y
    sticks += coals
    a = sticks - 1
    b = x - 1
    ops = (a + b - 1) // b
    print(ops + k)

t = int(input())
for _ in range(t):
    main()
