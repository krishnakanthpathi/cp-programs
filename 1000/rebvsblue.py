
import math

def main():
    n , r , b = map(int, input().split())

    res = ""
    parts = r // (b + 1)
    extra = r % (b + 1)
    for i in range(b  + 1):  

        res += "R" * parts
        res += "R" * (1 if extra > 0 else 0)
        extra -= 1
        if i < b:
            res += "B"
   
    ans = (res + "R" * extra) 
    print(ans)
if __name__ == "__main__":
    for _ in range(int(input())):
        main()