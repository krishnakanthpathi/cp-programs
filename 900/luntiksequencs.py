

def main():
    n = int(input())    
    arr = [int(val) for val in input().split()]
    ones = arr.count(1)
    zeros = arr.count(0)
    
    print(ones * (2 ** zeros))
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()