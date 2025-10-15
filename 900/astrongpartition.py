import math

def main():
    n , x = map(int, input().split())
    arr = list(map(int, input().split()))
    maxi = sum([ math.ceil(i/x) for i in arr])
    mini = math.ceil(sum(arr)/x)
    print(mini, maxi)
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()