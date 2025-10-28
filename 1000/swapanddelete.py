
def main():
    string = input().strip()
    zeros = string.count('0')
    ones = len(string) - zeros
    res = 0
    for val in string :
        if val == '0':
            ones -= 1
        else:
            zeros -= 1
        if ones < 0 or zeros < 0:
            res += 1

    print(res)
    
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()