

def main():
    string = input().strip()
    ones = string.count('1')
    zeros = string.count('0')
    
    if min(ones, zeros) % 2 == 1:
        print("DA")
    else:
        print("NET")
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()