


def area(x1 , y1 , x2 , y2 , x3 , y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) )

def find_area(side1 , side2) :
    x1 , y1 = side1[0]
    x2 , y2 = side1[-1]
    a = 0
    for point in side2:
        x3 , y3 = point
        a = max(a , area(x1 , y1 , x2 , y2 , x3 , y3))
    return a

def main():
    n , m = map(int, input().split())
    arr = list(map(int, input().split()))
    bottom = []
    for i in range(1 , len(arr)):
        bottom.append((arr[i] , 0))
    top = []
    arr = list(map(int, input().split()))
    for i in range(1 , len(arr)):
        top.append((arr[i] , m))
    left = []
    arr = list(map(int, input().split()))
    for i in range(1 , len(arr)):
        left.append((0 , arr[i]))
    right = []
    arr = list(map(int, input().split()))
    for i in range(1 , len(arr)):
        right.append((n , arr[i]))

    ans = 0
    ans = max(ans , find_area(bottom , top))
    ans = max(ans , find_area(top , bottom))
    ans = max(ans , find_area(right , left))
    ans = max(ans , find_area(left , right))
    print(ans)
if __name__ == "__main__":
    for _ in range(int(input())):
        main()