
def main():
    a , b = map(int, input().split())
    diff = abs(a - b)
    if diff == 0 :
        print(0,0)
        return  
    print( diff , min( b%diff , diff - b%diff ) )
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()